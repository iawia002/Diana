import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import 'normalize.css';

import registerServiceWorker from 'src/registerServiceWorker';
import { NotFound, FriendsView } from 'src/common/common';
import Index from 'src/blog/Index';
import ArticleView from 'src/blog/Article';
import TagsView from 'src/blog/Tags';
import TagView from 'src/blog/Tag';
import EditorView from 'src/blog/Editor';

import FishIndex from 'src/fish/Index';
import FishArticleView from 'src/fish/Article';

import LoginView from 'src/auth/Login';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Index} />
        <Route exact={true} path="/friends" component={FriendsView} />
        <Route exact={true} path="/p/:id" component={ArticleView} />
        <Route exact={true} path="/tags" component={TagsView} />
        <Route exact={true} path="/tag/:tag" component={TagView} />
        <Route exact={true} path="/p/:id/edit" component={EditorView} />
        <Route exact={true} path="/fish" component={FishIndex} />
        <Route exact={true} path="/fish/p/:id" component={FishArticleView} />
        <Route exact={true} path="/auth/login" component={LoginView} />
        <Route component={NotFound} />
      </Switch>
    </BrowserRouter>
  );
};

ReactDOM.render(<AppRouter />, document.getElementById('root') as HTMLElement);
registerServiceWorker();
