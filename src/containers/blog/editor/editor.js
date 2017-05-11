import 'notie/dist/notie.min.css';

import $ from 'jquery';
import notie from 'notie';
import marked from 'marked';
import hljs from 'highlight.js';
import utils from '../../utils';


hljs.configure({
  tabReplace: '    ',
});

const renderer = new marked.Renderer();
marked.setOptions({
  renderer,
  gfm: true,
  tables: true,
  breaks: true,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  langPrefix: 'hljs ',
  highlight: (code, lang) => {
    const autoFunc = hljs.highlightAuto(code, [lang]).value;
    return autoFunc;
  },
});


export default class Editor {
  constructor() {
    this.save = this.save.bind(this); // 防止别的方法来调这个函数时 this 会出错
  }

  render() {
    $('#output').html(marked($('#markdown_content').val()));
  }

  // eslint-disable-next-line
  getTags() {
    const tags = [];
    $('ul').last().children('li').each((index, element) => {
      tags.push($(element).text());
    });
    return tags;
  }

  save() {
    const self = this;
    self.render();
    const tags = self.getTags();
    $('#output ul').last().remove();
    const xsrf = utils.getCookie('_xsrf');
    const articleID = $('#article_id').val();
    $.post({
      url: `/p/${articleID}/edit`,
      data: {
        article_id: articleID,
        title: $('#output h1').html(),
        introduction: $('#output blockquote').html() ? $('#output blockquote').html() : '',
        markdown_content: $('#markdown_content').val(),
        compiled_content: $('#output').html(),
        tags,
        _xsrf: xsrf,
      },
      success: () => {
        notie.alert({ type: 'success', text: 'success' });
      },
      error: () => {
        notie.alert({ type: 'error', text: 'error' });
      },
    });
  }
}
