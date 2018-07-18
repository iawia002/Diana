import * as React from 'react';

import { Article, User } from 'src/blog/Interface';
const styles = require('src/blog/styles/components.scss');
const articleStyles = require('src/blog/styles/article.scss');

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
        className={articleStyles.article}
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
        <div className={articleStyles.tags}>{tags}</div>
        <p className={articleStyles.time}>
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
        <div className={`${articleStyles.rightWrapper} hidden-xs`}>
          <div
            className={articleStyles.right}
            style={{
              backgroundImage:
                'url("http://img.l.jifangcheng.com/448306d943165b8c281583c854d06be5e204de8b.png")',
            }}
          >
            <div
              className={articleStyles.avatar}
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
        <div className={`${articleStyles.topNav} visible-xs`}>
          <div
            className={articleStyles.avatar}
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

export class Nav extends React.Component<{}, {}> {
  render() {
    return (
      <nav className={styles.nav}>
        <li className={styles.category}>
          <a href="/">首页</a>
          <a href="/tags">标签</a>
          <a href="/p/78">我的项目</a>
          <a href="/p/76">工具</a>
          <a href="/friends">朋友们</a>
          <a
            href="https://github.com/iawia002/Diana"
            className={styles.emoji}
            target="_blank"
            data-balloon="GitHub @iawia002"
            data-balloon-pos="left"
          >
            <i className="fa fa-github" aria-hidden="true" />
          </a>
          <a
            href="mailto:%7a%32%64@%6a%69%66%61%6e%67%63%68%65%6e%67.%63%6f%6d"
            className={styles.emoji}
            data-balloon="z2d@jifangcheng.com"
            data-balloon-pos="left"
          >
            <i className="fa fa-envelope-o" aria-hidden="true" />
          </a>
        </li>
      </nav>
    );
  }
}
