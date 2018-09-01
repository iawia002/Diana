import * as React from 'react';
import { Redirect } from 'react-router-dom';
import { AxiosResponse, AxiosError } from 'axios';
const notie = require('notie');

import { request } from 'src/request';

const styles = require('src/auth/styles/login.scss');

interface LoginState {
  username: string;
  password: string;
  login: boolean;
}

export default class LoginView extends React.Component<{}, LoginState> {
  constructor(props: {}) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.state = {
      username: '',
      password: '',
      login: false,
    };
  }

  componentDidMount() {
    document.title = '登录 - iawia002';
  }

  handleChange(event: React.FormEvent<HTMLInputElement>) {
    const { name, value } = event.currentTarget;
    var state = {};
    state[name] = value;
    this.setState(state);
  }

  handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    const { username, password } = this.state;
    const self = this;
    request
      .post('/auth/login/', {
        username,
        password,
      })
      .then(function(response: AxiosResponse) {
        notie.alert({ type: 'success', text: '登录成功' });
        self.setState({ login: true });
      })
      .catch(function(error: AxiosError) {
        console.log(error);
        notie.alert({ type: 'error', text: '登录失败' });
      });
    event.preventDefault();
  }

  render() {
    if (this.state.login) {
      return <Redirect to="/" />;
    }
    return (
      <div className={styles.top}>
        <div className={styles.login}>
          <div
            className={styles.avatar}
            style={{
              backgroundImage:
                'url("http://img.l.jifangcheng.com/3306700a34d503e000b41e3a7060d59c6dbc8308.png")',
            }}
          />
          <form onSubmit={this.handleSubmit}>
            <input
              type="text"
              name="username"
              placeholder="用户名"
              value={this.state.username}
              onChange={this.handleChange}
            />
            <input
              type="password"
              name="password"
              placeholder="密码"
              value={this.state.password}
              onChange={this.handleChange}
            />
            <button type="submit">登录</button>
          </form>
        </div>
      </div>
    );
  }
}
