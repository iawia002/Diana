import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Index from './blog/Index';
import ArticleView from './blog/Article';
import TagsView from './blog/Tags';
import TagView from './blog/Tag';
import EditorView from './blog/Editor';
import registerServiceWorker from './registerServiceWorker';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Index} />
        <Route exact={true} path="/p/:id" component={ArticleView} />
        <Route exact={true} path="/tags" component={TagsView} />
        <Route exact={true} path="/tag/:tag" component={TagView} />
        <Route exact={true} path="/p/:id/edit" component={EditorView} />
      </Switch>
    </BrowserRouter>
  );
};

ReactDOM.render(
  <AppRouter />,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();
