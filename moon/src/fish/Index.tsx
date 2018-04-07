import * as React from 'react';
import axios, { AxiosResponse, AxiosError }  from 'axios';

import  { LoadMoreView } from './utils';
import { ArticleListView, Footer, FishTop } from './components';

import './styles/base.scss';

export default class FishIndex extends LoadMoreView<{}> {
  constructor(props: {}) {
    super(props);
  }

  componentDidMount() {
    document.title = '知乎热门钓鱼帖 - L';
    super.componentDidMount.apply(this);
    var self = this;
    axios.get('http://0.0.0.0:8004/fish')
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data});
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
      <FishTop />
      <div className="main">
        <ArticleListView articles={data.articles} />
        <Footer/>
      </div>
      </>
    );
  }
}
