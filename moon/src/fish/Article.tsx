import * as React from 'react';
import { match } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';
import { Helmet } from 'react-helmet';

import { request } from 'src/request';
import { Article } from 'src/fish/Interface';
import { ArticleContentView, Footer, Top } from 'src/fish/components';
import { ImageGallery } from 'src/components/ImageGallery';
import 'lazysizes';

const styles = require('src/fish/styles/article.scss');

interface MatchParams {
  id: string;
}

interface State {
  article: Article;
}

interface Props {
  match: match<MatchParams>;
  setSelector(selector: HTMLDivElement, attr: string): void;
}

class FishArticleView extends React.Component<Props, { data: State }> {
  private selector: HTMLDivElement;

  componentDidMount() {
    const { id } = this.props.match.params;
    var self = this;
    request
      .get(`/fish/p/${id}`)
      .then(function(response: AxiosResponse) {
        self.setState({ data: response.data });
        document.title = `${response.data.article.title} - 知乎热门钓鱼帖 - L`;
      })
      .catch(function(error: AxiosError) {
        console.log(error);
      });
  }

  proc(wrappedComponentInstance: ArticleContentView) {
    if (wrappedComponentInstance && !this.selector) {
      this.selector = wrappedComponentInstance.selector;
      this.props.setSelector(this.selector, 'data-src');
    }
  }

  render() {
    const { state } = this;
    if (!state) {
      return <div />;
    }
    const { article } = state.data;
    return (
      <>
        <Helmet>
          <meta name="referrer" content="no-referrer" />
        </Helmet>
        <Top />
        <div className={styles.main}>
          <ArticleContentView
            article={article}
            listMode={false}
            ref={ref => this.proc(ref as ArticleContentView)}
          />
          <Footer />
        </div>
      </>
    );
  }
}

export default ImageGallery(FishArticleView);
