var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./common');

var serverHost = '0.0.0.0';

new WebpackDevServer(webpack(config), config.devServer)
  .listen(config.devServer.port, serverHost, function (err) {
    if (err) {
      console.log(err);
    } else {
      console.log('==> 🐶  Static file server started at http://' + serverHost + ':' + config.devServer.port);
    }
  });
