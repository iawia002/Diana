import * as React from 'react';

import { Article, User } from './Interface';

interface ContentProps {
  article: Article;
  login: boolean;
  listMode: boolean;
}

export class ArticleContentView extends React.Component<ContentProps, {}> {
  public selector: HTMLDivElement;
  render() {
    const { article, login, listMode } = this.props;
    var tags = [];
    for (var tag of article.tags) {
      tags.push(
        <a href={`/tag/${tag.url}`} key={tag.tag_id}>
          {tag.content}
          <span>{tag.number}</span>
        </a>
      );
    }
    return (
      <div
        className="article"
        ref={ref => (this.selector = ref as HTMLDivElement)}
      >
        {listMode ? (
          <>
            <h1>
              <a href={`/p/${article.article_id}`}>{article.title}</a>
            </h1>
            <blockquote
              dangerouslySetInnerHTML={{
                __html: article.introduction ? article.introduction : '',
              }}
            />
          </>
        ) : (
          <div dangerouslySetInnerHTML={{ __html: article.compiled_content }} />
        )}
        <div className="tags">{tags}</div>
        <p className="time">
          <span>
            <i className="fa fa-eye" aria-hidden="true" /> {article.views}
          </span>
          <span>
            <i className="fa fa-calendar" aria-hidden="true" />{' '}
            {article.update_time}
          </span>
          {login ? (
            <span>
              <a href={`/p/${article.article_id}/edit`} target="_blank">
                编辑
              </a>
            </span>
          ) : (
            ''
          )}
        </p>
      </div>
    );
  }
}

interface Props {
  articles: Array<Article>;
  login: boolean;
}

export class ArticleListView extends React.Component<Props, {}> {
  render() {
    const { articles, login } = this.props;
    var elements = [];
    for (var article of articles) {
      elements.push(
        <ArticleContentView
          key={article.article_id}
          article={article}
          login={login}
          listMode={true}
        />
      );
    }
    return <>{elements}</>;
  }
}

export class RightView extends React.Component<{ user: User }, {}> {
  render() {
    const { user } = this.props;
    return (
      <>
        <div className="right-wrapper hidden-xs">
          <div
            className="right"
            style={{
              backgroundImage:
                'url("http://img.l.jifangcheng.com/448306d943165b8c281583c854d06be5e204de8b.png")',
            }}
          >
            <div
              className="avatar"
              style={{ backgroundImage: `url(${user.avatar})` }}
            />
            <h1>{user.username}</h1>
            <p>{user.introduction}</p>
            <ul>
              <li>
                <a href="/">首页</a>
              </li>
              <li>
                <a href="/tags">所有标签</a>
              </li>
            </ul>
          </div>
        </div>
        <div className="top-nav visible-xs">
          <div
            className="avatar"
            style={{ backgroundImage: `url(${user.avatar})` }}
          />
          <h1>
            <a href="/">{user.username}</a>
          </h1>
          <p>{user.introduction}</p>
        </div>
      </>
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
