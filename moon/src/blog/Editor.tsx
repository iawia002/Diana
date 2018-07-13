import * as React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';
import * as marked from 'marked';
import * as hljs from 'highlight.js';
import { UnControlled as CodeMirror, IInstance } from 'react-codemirror2';
import { ScrollInfo } from 'codemirror';
var notie = require('notie');

import { request } from '../request';
import { getCookie } from '../utils';

import 'codemirror/mode/gfm/gfm';
import 'highlight.js/styles/solarized-dark.css';
import 'codemirror/lib/codemirror.css';
import 'notie/dist/notie.min.css';

import './styles/editor.scss';

interface MatchParams {
  id: string;
}

interface State {
  article_id: number;
  article_markdown_content: string;
  article_title: string;
  rendered: string;
}

const renderer = new marked.Renderer();
const md = marked.setOptions({
  renderer,
  gfm: true,
  tables: true,
  breaks: true,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  langPrefix: 'hljs ',
  highlight: (code: string, lang: string) => {
    const autoFunc = hljs.highlightAuto(code, [lang]).value;
    return autoFunc;
  },
});

export default class EditorView extends React.Component<
  RouteComponentProps<MatchParams>,
  State
> {
  private output: HTMLDivElement | null;

  constructor(props: RouteComponentProps<MatchParams>) {
    super(props);
    this.save = this.save.bind(this);
  }

  componentDidMount() {
    document.title = '编辑 - L';
    const { id } = this.props.match.params;
    const self = this;
    request
      .get(`/p/${id}/edit`)
      .then(function(response: AxiosResponse) {
        self.setState({
          article_id: response.data.article_id,
          article_markdown_content:
            response.data.article_markdown_content || '',
          article_title: response.data.article_id || '',
          rendered: md.parse(response.data.article_markdown_content || ''),
        });
      })
      .catch(function(error: AxiosError) {
        console.log(error);
      });
  }

  handleScroll(editor: IInstance, data: ScrollInfo) {
    const percentage = data.top / (data.height - data.clientHeight);
    const node = this.output as HTMLElement;
    const outputHeight = node.scrollHeight - node.offsetHeight;
    node.scrollTo({ top: percentage * outputHeight });
  }

  handleRender(value: string) {
    this.setState({
      article_markdown_content: value,
      rendered: md.parse(value),
    });
  }

  save() {
    const { article_id, article_markdown_content } = this.state;
    const xsrf = getCookie('_xsrf');
    const node = this.output as HTMLElement;
    node.innerHTML = md.parse(article_markdown_content);
    // get tags
    var tags = [];
    const ul = node.getElementsByTagName('ul');
    if (ul.length > 0) {
      const tagNodes = ul[ul.length - 1].getElementsByTagName('li');
      for (var i = 0; i < tagNodes.length; i++) {
        tags.push(tagNodes[i].innerText);
      }
      // remove tags (ul[-1])
      node.removeChild(ul[ul.length - 1]);
    }

    const data = {
      article_id: article_id,
      title: node.getElementsByTagName('h1')[0].innerHTML,
      introduction: node.getElementsByTagName('blockquote')[0]
        ? node.getElementsByTagName('blockquote')[0].innerHTML
        : '',
      markdown_content: article_markdown_content,
      compiled_content: node.innerHTML,
      tags,
      _xsrf: xsrf,
    };

    request
      .post(`/p/${article_id}/edit`, data)
      .then(function(response: AxiosResponse) {
        notie.alert({ type: 'success', text: 'success' });
      })
      .catch(function(error: AxiosError) {
        console.log(error);
        notie.alert({ type: 'error', text: 'error' });
      });
  }

  render() {
    const { state } = this;
    if (!state) {
      return <div />;
    }
    return (
      <div className="editor-content">
        <div className="lbox">
          <a className="topbar" onClick={this.save}>
            <i className="fa fa-check" aria-hidden="true" /> 保存
          </a>
          <CodeMirror
            autoScroll={true}
            autoCursor={false}
            value={state.article_markdown_content}
            className="source"
            options={{
              mode: 'gfm',
              lineWrapping: true,
            }}
            onChange={(editor, data, value) => {
              this.handleRender(value);
            }}
            onScroll={(editor, data) => {
              this.handleScroll(editor, data);
            }}
          />
        </div>
        <div
          className="rbox"
          ref={output => (this.output = output)}
          dangerouslySetInnerHTML={{ __html: state.rendered }}
        />
      </div>
    );
  }
}
