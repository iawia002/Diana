import * as React from 'react';
import { AxiosResponse } from 'axios';

import { request } from './request';
import { Bg } from './blog/Interface';

const styles = require('./blog/styles/index.scss');

export class NotFound extends React.Component<{}, { data: Bg }> {
  componentDidMount() {
    var self = this;
    request.get('/bg').then(function(response: AxiosResponse) {
      self.setState({ data: response.data });
    });
  }

  render() {
    const { state } = this;
    if (!state) {
      return <div />;
    }
    const { data } = state;
    return (
      <div className={styles.top} style={{ height: '100%' }}>
        <div
          className={styles.bg}
          style={{ backgroundImage: `url(${data.url})` }}
        />
        <h1
          style={{
            fontSize: '5rem !important',
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
          }}
        >
          404
        </h1>
        <div className={styles.bottomConnect}>
          <a href="/" data-balloon="返回首页" data-balloon-pos="up">
            <i className="fa fa-paper-plane" aria-hidden="true" />
          </a>
          <a
            href="https://github.com/iawia002/Diana"
            target="_blank"
            data-balloon="GitHub @iawia002"
            data-balloon-pos="up"
          >
            <i className="fa fa-github" aria-hidden="true" />
          </a>
          <a
            href="mailto:%7a%32%64@%6a%69%66%61%6e%67%63%68%65%6e%67.%63%6f%6d"
            data-balloon="z2d@jifangcheng.com"
            data-balloon-pos="up"
          >
            <i className="fa fa-envelope-o" aria-hidden="true" />
          </a>
        </div>

        <p className={styles.bgIntro}>{data.name}</p>
      </div>
    );
  }
}
