var path = require('path');
var autoprefixer = require('autoprefixer');
var postcssImport = require('postcss-import');
var merge = require('webpack-merge');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var webpack = require('webpack');
var development = require('./dev.js');
var production = require('./prod.js');

var TARGET = process.env.npm_lifecycle_event;

var PATHS = {
  app: path.join(__dirname, '../src/js/containers/'),
  build: path.join(__dirname, '../static/dist/'),
  nodeModules: path.join(__dirname, '../node_modules/'),
};

var VENDOR = [
  'jquery',
  'highlight.js',
];

var common = {
  entry: {
    // app: [PATHS.app],
    vendor: VENDOR,
    editor: [PATHS.app + 'editor'],
    article: [PATHS.app + 'article'],
    index: [PATHS.app + 'index'],
    tag: [PATHS.app + 'tag'],
    tags: [PATHS.app + 'tags'],
    login: [PATHS.app + 'login'],
    error: [PATHS.app + 'error'],
  },

  output: {
    filename: '[name].[chunkhash].js',
    path: PATHS.build,
  },

  plugins: [
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/editor.html'),
      hash: true,
      filename: 'editor.html',
      chunks: ['vendor', 'editor', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/article.html'),
      hash: true,
      filename: 'article.html',
      chunks: ['vendor', 'article', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/index.html'),
      hash: true,
      filename: 'index.html',
      chunks: ['vendor', 'index', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/tag.html'),
      hash: true,
      filename: 'tag.html',
      chunks: ['vendor', 'tag', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/tags.html'),
      hash: true,
      filename: 'tags.html',
      chunks: ['vendor', 'tags', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/login.html'),
      hash: true,
      filename: 'login.html',
      chunks: ['vendor', 'login', 'commons'],
      inject: 'body'
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/error.html'),
      hash: true,
      filename: 'error.html',
      chunks: ['vendor', 'error', 'commons'],
      inject: 'body'
    }),

    // 只是把模板文件移到 dist 目录
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/article_list.html'),
      filename: 'article_list.html',
      inject: false
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/footer.html'),
      filename: 'footer.html',
      inject: false
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/right.html'),
      filename: 'right.html',
      inject: false
    }),
    new HtmlWebpackPlugin({
      template: path.join(__dirname, '../src/templates/scrollreveal.html'),
      filename: 'scrollreveal.html',
      inject: false
    }),

    new webpack.optimize.CommonsChunkPlugin({name: 'vendor', filename: 'vendor.[hash].js'}),
    // new webpack.optimize.CommonsChunkPlugin({name: 'commons', filename: 'commons.[chunkhash].js'}),

    new ExtractTextPlugin('[name].[contenthash].css'),

    // new webpack.ProvidePlugin({
    //   $: "jquery",
    //   jQuery: "jquery"
    // })
  ],

  resolve: {
    extensions: ['', '.js', '.jsx', '.coffee'],
    modulesDirectories: ['node_modules', PATHS.app],
  },

  module: {
    preLoaders: [
    ],
    loaders: [
      {
        test: /\.html$/,
        loader: "raw-loader"
      },
      {
        test: /\.(css|sass|scss)$/,
        loader: ExtractTextPlugin.extract("style-loader", ["css-loader", "postcss-loader", "sass-loader"])
      },
      {
        test: /\.(jpe?g|png|gif|bmp|ico)$/i,
        loader: 'file?name=img/[name].[ext]',
      },
      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader?limit=10000&minetype=application/font-woff',
      },
      {
        test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader?limit=10000&minetype=application/octet-stream',
      },
      {
        test: /\.svg(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader?limit=10000&minetype=application/font-woff',
      },
      {
        test: /\.json(\?.*)?$/,
        loader: 'file-loader?name=/files/[name].[ext]'
      },
      {
        test: /\.coffee$/,
        exclude: /(node_modules|bower_components)/,
        loader: "coffee",
        // loaders: ["coffee", "babel"],
        // query: {
        //   presets: ['es2015']
        // }
      }
    ]
  },

  postcss: function(webpack) {
    return [
      postcssImport({
        addDependencyTo: webpack
      }),
      autoprefixer()
    ]
  },
  devServer: {
    contentBase: PATHS.app,
    hot: true,
    port: 9000,
    noInfo: false,
    // quiet: true,
    historyApiFallback: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    stats: {
      colors: true,
    },
  },
};

if (TARGET === 'dev') {
  module.exports = merge(development, common);
}

if (TARGET === 'build' || TARGET === 'd') {
  module.exports = merge(production, common);
}
