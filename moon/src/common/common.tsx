import * as React from 'react';
import { AxiosResponse } from 'axios';
const Disqus = require('disqus-react');

import { request } from 'src/request';
import { Bg } from 'src/blog/Interface';
import { Nav } from 'src/blog/components';
import { Footer } from 'src/components/components';

const styles = require('src/common/styles/common.scss');
const blogStyles = require('src/blog/styles/index.scss');

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
      <div className={blogStyles.top} style={{ height: '100%' }}>
        <div
          className={blogStyles.bg}
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
        <div className={blogStyles.bottomConnect}>
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

        <p className={blogStyles.bgIntro}>{data.name}</p>
      </div>
    );
  }
}

export class FriendsView extends React.Component<{}, {}> {
  componentDidMount() {
    document.title = '朋友们 - iawia002';
  }

  render() {
    const disqusShortname = 'theycallmel';
    const disqusConfig = {
      url: `https://l.jifangcheng.com/friends`,
      identifier: 'friends',
      title: '朋友们',
    };
    return (
      <>
        <div className={blogStyles.top} style={{ height: '30%' }}>
          <div
            className={blogStyles.bg}
            style={{
              backgroundImage:
                'url(http://img.l.jifangcheng.com/68ae837e8306c7a75261ebd18d8b2c352aec2442.png)',
            }}
          />
          <Nav />
          <div className={blogStyles.mainContent} style={{ marginTop: 0 }}>
            <h1 style={{ fontSize: '1.5rem' }}>“以我所有，换我所无”</h1>
          </div>
        </div>
        <div className={styles.content}>
          {/* <h1>Boy♂Next♂Door</h1> */}
          <h1>B♂ys</h1>
          <div className={styles.card}>
            <img
              className={styles.avatar}
              src="https://avatars0.githubusercontent.com/u/16148054?s=460&v=4"
            />
            <a target="_blank" href="https://2heng.xin">
              Mashiro
            </a>
            <p>You got to put the past behind you before you can move on</p>
          </div>
          <div className={styles.card}>
            <img
              className={styles.avatar}
              src="https://avatars1.githubusercontent.com/u/1023481?s=460&v=4"
            />
            <a target="_blank" href="http://blog.defcoding.com">
              runforever
            </a>
            <p>to be a rock star</p>
          </div>
          <div className={styles.card}>
            <img
              className={styles.avatar}
              src="https://avatars1.githubusercontent.com/u/29391378?s=200&v=4"
            />
            <a target="_blank" href="https://blog.yuntianti.com/">
              Tech Forever
            </a>
            <p>Tech Forever Team</p>
          </div>
          <h1>
            留言 <span>（Disqus 不稳定，可能需要科学上网）</span>
          </h1>
          <div className={styles.comment}>
            <Disqus.DiscussionEmbed
              shortname={disqusShortname}
              config={disqusConfig}
            />
          </div>

          <Footer />
        </div>
      </>
    );
  }
}
