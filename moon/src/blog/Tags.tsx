import * as React from 'react';
import { AxiosResponse, AxiosError } from 'axios';

import { request } from '../request';
import { Tags } from './Interface';
import { RightView, Footer } from './components';

const styles = require('./styles/article.scss');

export default class TagsView extends React.Component<{}, { data: Tags }> {
  componentDidMount() {
    document.title = '所有标签 - L';
    var self = this;
    request
      .get('/tags')
      .then(function(response: AxiosResponse) {
        self.setState({ data: response.data });
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
    const { keys, values, user } = state.data;
    var keyElements = [];
    for (var key of keys) {
      keyElements.push(
        <li key={key}>
          <a href={`#${key}`}>{key}</a>
        </li>
      );
    }
    var valueElements = [];
    for (var value of values) {
      var tags = [];
      for (var tag of value[1]) {
        tags.push(
          <a key={tag.tag_id} href={`/tag/${tag.url}`}>
            {tag.content}
            <span>{tag.number}</span>
          </a>
        );
      }
      valueElements.push(
        <div key={value[0]}>
          <hr />
          <p id={value[0]}>
            <a href={`#${value[0]}`}>{value[0]}</a>
          </p>
          <div className={styles.tags}>{tags}</div>
        </div>
      );
    }
    return (
      <div className={[styles.flexArticle, styles.grayBg].join(' ')}>
        <RightView user={user} />
        <div className={styles.left}>
          <div className={styles.tagNav}>
            <p>所有标签</p>
          </div>
          <div className={[styles.article, styles.allTags].join(' ')}>
            <ul>{keyElements}</ul>

            {valueElements}
          </div>
          <Footer />
        </div>
      </div>
    );
  }
}
