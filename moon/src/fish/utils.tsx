import * as React from 'react';
import { AxiosResponse }  from 'axios';

import { request } from '../request';
import { State } from './Interface';

export class LoadMoreView<P> extends React.Component<P, State> {
  componentDidMount() {
    window.addEventListener('scroll', this.handleScroll.bind(this));
  }

  loadMore(nextPage: number) {
    var self = this;
    request.get('/fish/more', {params: {next_page: nextPage}})
      .then(function (response: AxiosResponse) {
        if (!response.data.articles) {
          return;
        }
        let { data } = self.state;
        data.next_page = response.data.next_page;
        data.articles = data.articles.concat(response.data.articles);
        self.setState({ data });
      });
  }

  handleScroll() {
    const { data } = this.state;
    const scrollTop = window.scrollY;
    const scrollHeight = window.document.body.scrollHeight;
    const windowHeight = window.document.body.offsetHeight;
    if (scrollTop + windowHeight === scrollHeight) {
      this.loadMore(data.next_page);
    }
  }
}
