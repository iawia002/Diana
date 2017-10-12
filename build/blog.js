const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


const PATHS = {
  app: path.join(__dirname, '../src/containers/blog/'),
  build: path.join(__dirname, '../static/dist/blog/'),
};

module.exports = {
  paths: PATHS,
  publicPath: '/static/dist/blog/',
  entry: {
    vendor: [
      'jquery',
      'highlight.js',
      'normalize.css',
      'marked',  // webpack 第一次打包的时候没有处理这个库，--watch 再随便保存一个文件它又会打包，那时候又处理了这个库，现在不知道什么原因，只能先把它加到这里，暂时解决了这个问题
    ],
    editor: [`${PATHS.app}editor`],
    article: [`${PATHS.app}article`],
    index: [`${PATHS.app}index`],
    tag: [`${PATHS.app}tag`],
    tags: [`${PATHS.app}tags`],
    error: [`${PATHS.app}error`],
  },

  plugins: [
    new CleanPlugin(['blog'], {
      root: path.join(__dirname, '../static/dist'),
      verbose: true,
      dry: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/editor.html'),
      hash: true,
      filename: 'editor.html',
      chunks: ['vendor', 'editor', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/article.html'),
      hash: true,
      filename: 'article.html',
      chunks: ['vendor', 'article', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/index.html'),
      hash: true,
      filename: 'index.html',
      chunks: ['vendor', 'index', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/tag.html'),
      hash: true,
      filename: 'tag.html',
      chunks: ['vendor', 'tag', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/tags.html'),
      hash: true,
      filename: 'tags.html',
      chunks: ['vendor', 'tags', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/error.html'),
      hash: true,
      filename: 'error.html',
      chunks: ['vendor', 'error', 'commons'],
      inject: 'body',
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/statistics.html'),
      hash: true,
      filename: 'statistics.html',
      chunks: ['vendor', 'commons'],
      inject: 'body',
    }),

    // 只是把模板文件移到 dist 目录
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/article_list.html'),
      filename: 'article_list.html',
      inject: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/footer.html'),
      filename: 'footer.html',
      inject: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/right.html'),
      filename: 'right.html',
      inject: false,
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/blog/scrollreveal.html'),
      filename: 'scrollreveal.html',
      inject: false,
    }),
  ],
};
