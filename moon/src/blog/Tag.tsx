import * as React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import axios, { AxiosResponse, AxiosError }  from 'axios';

import  { LoadMoreView } from './utils';
import { ArticleListView, Footer, RightView } from './components';

import './styles/article.scss';

interface MatchParams {
  tag: string;
}

export default class TagView extends LoadMoreView<RouteComponentProps<MatchParams>> {
  componentDidMount() {
    super.componentDidMount.apply(this);
    const { tag } = this.props.match.params;
    var self = this;
    axios.get(`http://0.0.0.0:8004/tag/${tag}`)
      .then(function (response: AxiosResponse) {
        self.setState({
          data: response.data,
          page: 'tag',
          tag: response.data.tag
        });
        document.title = `${response.data.tag} - L`;
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
    const { login, articles, user } = state.data;
    return (
      <div className="flex-article gray-bg">
        <RightView user={user} />
        <div className="left">
          <ArticleListView login={login} articles={articles} />
          <Footer/>
        </div>
      </div>
    );
  }
}
