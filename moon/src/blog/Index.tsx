import * as React from 'react';
import { AxiosResponse, AxiosError } from 'axios';

import { request } from '../request';
import  { LoadMoreView } from './utils';
import { ArticleListView, Footer } from './components';

import 'balloon-css/balloon.css';
import 'font-awesome/css/font-awesome.css';
import './styles/index.scss';

export default class Index extends LoadMoreView<{}> {
  constructor(props: {}) {
    super(props);
  }

  componentDidMount() {
    super.componentDidMount.apply(this);
    var self = this;
    request.get('/')
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data, page: 'index' });
      })
      .catch(function (error: AxiosError) {
        console.log(error);
      });
  }

  render() {
    const { state } = this;
    if (!state) {
      return (<div/>);
    }
    const { data } = state;
    return (
      <>
      <div className="top">
        <div className="bg" style={{ backgroundImage: `url(${data.bg.url})` }} />
        <nav className="nav">
          <li className="category">
            <a href="/">首页</a>
            <a href="/tags">所有标签</a>
            <a href="/p/78">我的项目</a>
            <a href="/p/76">工具</a>
            <a href="/p/86">L and friends</a>
            <a
              href="https://github.com/iawia002/Diana"
              className="emoji"
              target="_blank"
              data-balloon="GitHub @iawia002"
              data-balloon-pos="left"
            >
              <i className="fa fa-github" aria-hidden="true" />
            </a>
            <a
              href="mailto:%7a%32%64@%6a%69%66%61%6e%67%63%68%65%6e%67.%63%6f%6d"
              className="emoji"
              data-balloon="z2d@jifangcheng.com"
              data-balloon-pos="left"
            >
              <i className="fa fa-envelope-o" aria-hidden="true" />
            </a>
          </li>
        </nav>
        <div className="main-content">
          <h1>{data.user.username}</h1>
          <div className="introduction" id="introduction">
            <p>{data.user.introduction}</p>
            {
              data.login ?
                <span><i className="fa fa-pencil-square-o" aria-hidden="true" /></span>
              : ''
            }
          </div>
        </div>
        <p className="bg-intro">{data.bg.name}</p>
      </div>
      <div className="content">
        <ArticleListView login={data.login} articles={data.articles} />
        <Footer/>
      </div>
      </>
    );
  }
}
