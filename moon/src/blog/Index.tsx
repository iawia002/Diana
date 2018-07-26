import * as React from 'react';
import { AxiosResponse, AxiosError } from 'axios';

import { request } from 'src/request';
import { LoadMoreView } from 'src/blog/utils';
import { ArticleListView, Nav } from 'src/blog/components';
import { Footer } from 'src/components/components';

import 'balloon-css/balloon.css';
import 'font-awesome/css/font-awesome.css';
const styles = require('src/blog/styles/index.scss');

export default class Index extends LoadMoreView<{}> {
  constructor(props: {}) {
    super(props);
  }

  componentDidMount() {
    super.componentDidMount.apply(this);
    var self = this;
    request
      .get('/')
      .then(function(response: AxiosResponse) {
        self.setState({ data: response.data, page: 'index' });
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
    const { data } = state;
    return (
      <>
        <div className={styles.top}>
          <div
            className={styles.bg}
            style={{ backgroundImage: `url(${data.bg.url})` }}
          />
          <div className={styles.mask} />
          <Nav />
          <div className={styles.mainContent}>
            <div className={styles.introduction} id="introduction">
              <p>{`“${data.bg.quote}”`}</p>
            </div>
          </div>
          <p className={styles.bgIntro}>{data.bg.name}</p>
        </div>
        <div className={styles.content}>
          <ArticleListView login={data.login} articles={data.articles} />
          <Footer />
        </div>
      </>
    );
  }
}
