import * as React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';

import { request } from '../request';
import { Article, User } from './Interface';
import { ArticleContentView, Footer, RightView } from './components';

import 'highlight.js/styles/solarized-dark.css';
import './styles/article.scss';

interface MatchParams {
  id: string;
}

interface State {
  user: User;
  login: boolean;
  article: Article;
}

export default class ArticleView extends React.Component<
  RouteComponentProps<MatchParams>, {data: State}
> {
  componentDidMount() {
    const { id } = this.props.match.params;
    var self = this;
    request.get(`/p/${id}`)
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data });
        document.title = `${response.data.article.title} - L`;
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
    const { login, article, user } = state.data;
    return (
      <div className="flex-article gray-bg">
        <RightView user={user} />
        <div className="left">
          <ArticleContentView login={login} article={article} listMode={false} />
          <Footer/>
        </div>
      </div>
    );
  }
}
