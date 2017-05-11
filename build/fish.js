const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


const PATHS = {
  app: path.join(__dirname, '../src/containers/fish/'),
  build: path.join(__dirname, '../static/dist/fish/'),
};

module.exports = {
  paths: PATHS,
  publicPath: '/static/dist/fish/',
  entry: {
    vendor: [
      'jquery',
    ],
    article: [`${PATHS.app}article`],
    index: [`${PATHS.app}index`],
    error: [`${PATHS.app}error`],
  },

  plugins: [
    new CleanPlugin(['fish'], {
      root: path.join(__dirname, '../static/dist'),
      verbose: true,
      dry: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/article.html'),
      hash: true,
      filename: 'article.html',
      chunks: ['vendor', 'article'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/index.html'),
      hash: true,
      filename: 'index.html',
      chunks: ['vendor', 'index'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/error.html'),
      hash: true,
      filename: 'error.html',
      chunks: ['vendor', 'error'],
      inject: 'body'
    }),

    // 只是把模板文件移到 dist 目录
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/article_list.html'),
      filename: 'article_list.html',
      inject: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/footer.html'),
      filename: 'footer.html',
      inject: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/fish/top.html'),
      filename: 'top.html',
      inject: false,
    }),
  ],
};
