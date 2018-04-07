import * as React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import axios, { AxiosResponse, AxiosError }  from 'axios';
import { Helmet } from 'react-helmet';

import { Article } from './Interface';
import { ArticleContentView, Footer, FishTop } from './components';
import 'lazysizes';

import './styles/article.scss';

interface MatchParams {
  id: string;
}

interface State {
  article: Article;
}

export default class FishArticleView extends React.Component<
  RouteComponentProps<MatchParams>, {data: State}
> {
  componentDidMount() {
    const { id } = this.props.match.params;
    var self = this;
    axios.get(`http://0.0.0.0:8004/fish/p/${id}`)
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data });
        document.title = `${response.data.article.title} - 知乎热门钓鱼帖 - L`;
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
    const { article } = state.data;
    return (
      <>
      <Helmet>
        <meta name="referrer" content="no-referrer" />
      </Helmet>
      <FishTop />
      <div className="main">
        <ArticleContentView article={article} listMode={false} />
        <Footer/>
      </div>
      </>
    );
  }
}
