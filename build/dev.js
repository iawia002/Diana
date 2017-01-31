var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var path = require('path');
// var _ = require('lodash');
var array = require('lodash/array');
// var Dashboard = require('webpack-dashboard');
// var DashboardPlugin = require('webpack-dashboard/plugin');

// var dashboard = new Dashboard();

var PATHS = {
  app: path.join(__dirname, '../src/js/containers/')
};

var hot = [
  'webpack-dev-server/client?http://0.0.0.0:9000',
  'webpack/hot/dev-server',
];

module.exports = {
  entry: {
    editor: array.concat(hot, PATHS.app + 'editor'),
    article: array.concat(hot, PATHS.app + 'article'),
    index: array.concat(hot, PATHS.app + 'index'),
    tag: array.concat(hot, PATHS.app + 'tag'),
    tags: array.concat(hot, PATHS.app + 'tags'),
    login: array.concat(hot, PATHS.app + 'login'),
    error: array.concat(hot, PATHS.app + 'error'),
  },
  devtool: 'source-map',

  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"development"',
      },
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.HotModuleReplacementPlugin(),

    // new DashboardPlugin(dashboard.setData),
  ],
};
