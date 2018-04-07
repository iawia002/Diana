import * as React from 'react';

import { Article } from './Interface';

interface ContentProps {
  article: Article;
  listMode: boolean;
}

export class ArticleContentView extends React.Component<ContentProps, {}> {
  render() {
    const { article, listMode } = this.props;
    var imgs = [];
    for (var img of article.content) {
      imgs.push(<img data-src={img} className="lazyload" />);
    }
    return (
        <div className="article">
          <h1><a href={`/fish/p/${article.record_id}`}>{article.title}</a></h1>
          <p className="time">
            {article.image_num} 张图片 |&nbsp;
            {article.views} 次浏览 |&nbsp;
            更新于 {article.create_time} |&nbsp;
            <a href={article.source} target="_blank">来源</a>
          </p>
          {
            listMode ? '' : imgs
          }
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
        <ArticleContentView key={article.record_id} article={article} listMode={true} />
      );
    }
    return (
      <>
        {elements}
      </>
    );
  }
}

export class FishTop extends React.Component<{}, {}> {
  render() {
    return (
      <div className="fish-top">
        <div className="fish-avatar" />
        <h1><a href="/fish">知乎热门钓鱼帖</a></h1>
        <p>好好反省一下，别人怎么就能提那么多问题呢</p>
      </div>
    );
  }
}

export class Footer extends React.Component<{}, {}> {
  render() {
    return (
      <div className="footer">
        <p>Powered by ☕️ 🍔 and 🍦</p>
      </div>
    );
  }
}
