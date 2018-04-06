import * as React from 'react';
import axios, { AxiosResponse }  from 'axios';

import { Bg } from './blog/Interface';

export class NotFound extends React.Component<{}, {data: Bg}> {
  componentDidMount() {
    var self = this;
    axios.get('http://0.0.0.0:8004/bg')
      .then(function (response: AxiosResponse) {
        self.setState({ data: response.data });
      });
  }

  render() {
    const { state } = this;
    if (!state) {
      return (<div/>);
    }
    const { data } = state;
    return (
      <div className="top" style={{height: '100%'}}>
        <div className="bg" style={{ backgroundImage: `url(${data.url})` }} />
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
        <div className="bottom-connect">
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

        <p className="bg-intro">{data.name}</p>
      </div>
    );
  }
}
