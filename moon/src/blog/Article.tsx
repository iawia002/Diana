import * as React from 'react';
import { match } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';
const Disqus = require('disqus-react');

import { request } from 'src/request';
import { Article, User } from 'src/blog/Interface';
import { ArticleContentView, RightView } from 'src/blog/components';
import { ImageGallery } from 'src/components/ImageGallery';
import { Footer } from 'src/components/components';

import 'highlight.js/styles/solarized-dark.css';
const styles = require('src/blog/styles/article.scss');

interface MatchParams {
  id: string;
}

interface State {
  user: User;
  login: boolean;
  article: Article;
}

interface Props {
  match: match<MatchParams>;
  setSelector(selector: HTMLDivElement, attr: string): void;
}

class ArticleView extends React.Component<Props, { data: State }> {
  private selector: HTMLDivElement;

  proc(wrappedComponentInstance: ArticleContentView) {
    if (wrappedComponentInstance && !this.selector) {
      this.selector = wrappedComponentInstance.selector;
      this.props.setSelector(this.selector, 'src');
    }
  }

  componentDidMount() {
    const { id } = this.props.match.params;
    var self = this;
    request
      .get(`/p/${id}`)
      .then(function(response: AxiosResponse) {
        self.setState({ data: response.data });
        document.title = `${response.data.article.title} - iawia002`;
      })
      .catch(function(error: AxiosError) {
        console.log(error);
      });
  }

  render() {
    const { state } = this;
    if (!state) {
      return <div />;
    }
    const { login, article, user } = state.data;
    const disqusShortname = 'theycallmel';
    const disqusConfig = {
      url: `https://l.jifangcheng.com/p/${article.article_id}`,
      identifier: article.article_id,
      title: article.title,
    };
    return (
      <div className={[styles.flexArticle, styles.grayBg].join(' ')}>
        <RightView user={user} />
        <div className={styles.left}>
          <ArticleContentView
            login={login}
            article={article}
            listMode={false}
            ref={ref => this.proc(ref as ArticleContentView)}
          />
          <div className={styles.article} style={{ padding: '20px' }}>
            <Disqus.DiscussionEmbed
              shortname={disqusShortname}
              config={disqusConfig}
            />
          </div>
          <Footer />
        </div>
      </div>
    );
  }
}

export default ImageGallery(ArticleView);
