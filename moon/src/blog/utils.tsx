import * as React from 'react';
import axios, { AxiosResponse }  from 'axios';

import { State } from './Interface';

export class LoadMoreView<P> extends React.Component<P, State> {
  componentDidMount() {
    window.addEventListener('scroll', this.handleScroll.bind(this));
  }

  loadMore(nextPage: number, page: string, tag: string) {
    var self = this;
    axios.get('http://0.0.0.0:8004/more', {params: {next_page: nextPage, page, tag}})
      .then(function (response: AxiosResponse) {
        if (!response.data.articles) {
          return;
        }
        let { data } = self.state;
        data.login = response.data.login;
        data.next_page = response.data.next_page;
        data.articles = data.articles.concat(response.data.articles);
        self.setState({ data });
      });
  }

  handleScroll() {
    const scrollTop = window.scrollY;
    const scrollHeight = window.document.body.scrollHeight;
    const windowHeight = window.document.body.offsetHeight;
    if (scrollTop + windowHeight === scrollHeight) {
      this.loadMore(this.state.data.next_page, this.state.page, this.state.tag);
    }
  }
}
