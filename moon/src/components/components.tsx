import * as React from 'react';

const styles = require('src/components/styles/loading.scss');

export class Footer extends React.Component<{}, {}> {
  render() {
    return (
      <div className="footer">
        <p>Powered by ☕️ 🍔 and 🍦</p>
      </div>
    );
  }
}

export class Loading extends React.Component<{}, { emoji: string }> {
  constructor(props: {}) {
    super(props);
    this.state = { emoji: '🐳' };
  }
  componentDidMount() {
    var self = this;
    const emojis = [
      '😂',
      '🌚',
      '😕',
      '🤕',
      '👍️',
      '🤔',
      '🍪',
      '🔧',
      '✨',
      '🐳',
      '📝',
      '😉',
      '🙃',
      '😎',
      '🙋‍♂️',
      '🙋‍♀️',
      '😶',
      '😈',
      '🌕',
      '🌏',
      '💥',
      '🔥',
      '🌪',
      '🍞',
      '☕️',
      '🍭',
    ];
    window.setInterval(function() {
      self.setState({
        emoji: emojis[Math.floor(Math.random() * emojis.length)],
      });
    }, 1500);
  }

  render() {
    return (
      <div className={styles.loading}>
        <p>
          {this.state.emoji}
          <span>Loading</span>
        </p>
      </div>
    );
  }
}
