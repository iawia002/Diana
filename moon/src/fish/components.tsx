import * as React from 'react';

import { Article } from 'src/fish/Interface';

const styles = require('src/fish/styles/article.scss');

interface ContentProps {
  article: Article;
  listMode: boolean;
}

export class ArticleContentView extends React.Component<ContentProps, {}> {
  public selector: HTMLDivElement;
  render() {
    const { article, listMode } = this.props;
    var imgs = [];
    for (var i = 0; i < article.content.length; i++) {
      imgs.push(
        <img data-src={article.content[i]} className="lazyload" key={i} />
      );
    }
    return (
      <div
        className={styles.article}
        ref={ref => (this.selector = ref as HTMLDivElement)}
      >
        <h1>
          <a href={`/fish/p/${article.record_id}`}>{article.title}</a>
        </h1>
        <p className={styles.time}>
          {article.image_num} 张图片 |&nbsp;
          {article.views} 次浏览 |&nbsp; 更新于 {article.create_time} |&nbsp;
          <a href={article.source} target="_blank">
            来源
          </a>
        </p>
        {listMode ? '' : imgs}
      </div>
    );
  }
}

interface Props {
  articles: Array<Article>;
}

export class ArticleListView extends React.Component<Props, {}> {
  render() {
    const { articles } = this.props;
    var elements = [];
    for (var article of articles) {
      elements.push(
        <ArticleContentView
          key={article.record_id}
          article={article}
          listMode={true}
        />
      );
    }
    return <>{elements}</>;
  }
}

export class Top extends React.Component<{}, {}> {
  render() {
    return (
      <div className={styles.top}>
        <div className={styles.avatar} />
        <h1>
          <a href="/fish">知乎热门钓鱼帖</a>
        </h1>
        <p>好好反省一下，别人怎么就能提那么多问题呢</p>
      </div>
    );
  }
}
