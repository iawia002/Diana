import * as React from 'react';
import axios, { AxiosResponse, AxiosError }  from 'axios';

import { Tags } from './Interface';
import { RightView, Footer } from './components';

export default class TagsView extends React.Component<{}, {data: Tags}> {
  componentDidMount() {
    document.title = '所有标签 - L';
    var self = this;
    axios.get('http://0.0.0.0:8004/tags')
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data });
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
    const { keys, values, user } = state.data;
    var keyElements = [];
    for (var key of keys) {
      keyElements.push(
        <li key={key}><a href={`#${key}`}>{key}</a></li>
      );
    }
    var valueElements = [];
    for (var value of values) {
      var tags = [];
      for (var tag of value[1]) {
        tags.push(
          <a key={tag.tag_id} href={`/tag/${tag.url}`}>
            {tag.content}<span>{tag.number}</span>
          </a>
        );
      }
      valueElements.push(
        <div key={value[0]}>
          <hr />
          <p id={value[0]}><a href={`#${value[0]}`}>{value[0]}</a></p>
          <div className="tags">{tags}</div>
        </div>
      );
    }
    return (
      <div className="flex-article gray-bg">
        <RightView user={user} />
        <div className="left">
          <div className="tag-nav">
            <p>所有标签</p>
          </div>
          <div className="article all-tags">
            <ul>{keyElements}</ul>

            {valueElements}
          </div>
          <Footer/>
        </div>
      </div>
    );
  }
}
