const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


const PATHS = {
  app: path.join(__dirname, '../src/containers/fun/'),
  build: path.join(__dirname, '../static/dist/fun/'),
};

module.exports = {
  paths: PATHS,
  publicPath: '/static/dist/fun/',
  entry: {
    vendor: [
      'jquery',
    ],
    index: [`${PATHS.app}index`],
  },

  plugins: [
    new CleanPlugin(['fun'], {
      root: path.join(__dirname, '../static/dist'),
      verbose: true,
      dry: false,
    }),

    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fun/index.html'),
      hash: true,
      filename: 'index.html',
      chunks: ['vendor', 'index', 'commons'],
      inject: 'body',
    }),
  ],
};
