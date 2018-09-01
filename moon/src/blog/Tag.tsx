import * as React from 'react';
import { RouteComponentProps } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';

import { request } from 'src/request';
import { LoadMoreView } from 'src/blog/utils';
import { ArticleListView, RightView } from 'src/blog/components';
import { Footer, Loading } from 'src/components/components';

const styles = require('src/blog/styles/article.scss');

interface MatchParams {
  tag: string;
}

export default class TagView extends LoadMoreView<
  RouteComponentProps<MatchParams>
> {
  componentDidMount() {
    super.componentDidMount.apply(this);
    const { tag } = this.props.match.params;
    var self = this;
    request
      .get(`/tag/${tag}`)
      .then(function(response: AxiosResponse) {
        self.setState({
          data: response.data,
          page: 'tag',
          tag: response.data.tag,
        });
        document.title = `${response.data.tag} - iawia002`;
      })
      .catch(function(error: AxiosError) {
        console.log(error);
      });
  }

  render() {
    const { state } = this;
    if (!state) {
      return <Loading />;
    }
    const { login, articles, user } = state.data;
    return (
      <div className={[styles.flexArticle, styles.grayBg].join(' ')}>
        <RightView user={user} />
        <div className={styles.left}>
          <ArticleListView login={login} articles={articles} />
          <Footer />
        </div>
      </div>
    );
  }
}
