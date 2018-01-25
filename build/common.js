const path = require('path');
const webpack = require('webpack');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');


const appName = process.env.npm_package_config_app;
const app = require(`./${appName}.js`);  // eslint-disable-line

module.exports = (env) => {
  const DEBUG = env ? env.dev : false; // true or false
  const config = {
    entry: app.entry,

    output: {
      filename: '[name].[chunkhash].js',
      path: app.paths.build,
      publicPath: app.publicPath, // 在将 JS 文件插入到 HTML 中时会用到这个路径
    },

    plugins: [
      new webpack.optimize.OccurrenceOrderPlugin(),
      new UglifyJsPlugin({
        sourceMap: DEBUG,
        uglifyOptions: {
          compress: {
            warnings: DEBUG,
          },
        },
      }),

      new webpack.optimize.CommonsChunkPlugin({
        name: 'vendor',
        filename: 'vendor.[hash].js',
      }),
      // new webpack.optimize.CommonsChunkPlugin({
      //   name: 'commons', filename: 'commons.[chunkhash].js'
      // }),

      new ExtractTextPlugin('[name].[contenthash].css'),
    ].concat(app.plugins),

    resolve: {
      modules: ['node_modules'],
      extensions: ['.js', '.jsx', '.json', '.css', '.scss'],
      alias: {
        src: path.resolve(__dirname, '../src'),
      },
    },

    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /(node_modules|bower_components)/,
          use: [
            {
              loader: 'babel-loader',
              options: {
                presets: ['env'],
              },
            },
          ],
        },
        {
          test: /\.html$/,
          loader: 'raw-loader',
        },
        {
          test: /\.(css|sass|scss)$/,
          use: ExtractTextPlugin.extract({
            fallback: 'style-loader',
            use: [
              {
                loader: 'css-loader',
                options: {
                  importLoaders: 1,
                },
              },
              'postcss-loader',
              'sass-loader',
            ],
          }),
        },
        {
          test: /\.(jpe?g|png|gif|bmp|ico)$/i,
          loader: 'file-loader?name=img/[name].[ext]',
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
          loader: 'file-loader?name=/files/[name].[ext]',
        },
      ],
    },
  };
  if (DEBUG) {
    Object.assign(config, {
      devtool: 'source-map',
      watch: true,
      watchOptions: {
        aggregateTimeout: 1000, // 间隔单位 ms
        poll: true,
      },
    });
  }
  return config;
};
