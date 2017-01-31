var webpack = require('webpack');
var CleanPlugin = require('clean-webpack-plugin');
var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  output: {
    publicPath: '/static/dist/'  // 在将 JS 文件插入到 HTML 中时会用到这个路径
  },

  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"',
      },
    }),
    new CleanPlugin(['dist'], {
      root: path.join(__dirname, '../static/'),
      verbose: true,
      dry: false
    }),
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
  ],
};
