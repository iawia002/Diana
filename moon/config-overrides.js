module.exports = function override(config, env) {
  config.module.rules[1].oneOf.splice(
    config.module.rules[1].oneOf.length - 1,
    0,
    {
      test: /\.scss$/,
      use: [
        'style-loader',
        {
          loader: 'css-loader',
          options: {
            modules: true,
            sourceMap: process.env.NODE_ENV === 'production' ? false : true,
            importLoaders: 2,
            localIdentName: '[name]__[local]--[hash:base64:5]',
          },
        },
        'sass-loader',
      ],
    }
  );
  return config;
};
