const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


const PATHS = {
  app: path.join(__dirname, '../src/containers/auth/'),
  build: path.join(__dirname, '../static/dist/auth/'),
};

module.exports = {
  paths: PATHS,
  publicPath: '/static/dist/auth/',
  entry: {
    vendor: [
      'jquery',
    ],
    login: [`${PATHS.app}login`],
  },

  plugins: [
    new CleanPlugin(['auth'], {
      root: path.join(__dirname, '../static/dist'),
      verbose: true,
      dry: false,
    }),

    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/auth/login.html'),
      hash: true,
      filename: 'login.html',
      chunks: ['vendor', 'login', 'commons'],
      inject: 'body',
    }),
  ],
};
