require('./tag.coffee');
require('../common/more.coffee');

require('../../../css/article.scss');
require('font-awesome/css/font-awesome.css');

if (process.env.NODE_ENV !== 'production') {
  require('../../../templates/tag.html')
}
