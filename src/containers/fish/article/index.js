import 'lazysizes';
import $ from 'jquery';
import ImageGallery from 'src/containers/image_gallery';

import 'src/css/fish/article.scss';


$(document).ready(() => {
  $('p:has(img)').addClass('img');

  const iv = new ImageGallery('.article', 'data-src');
  iv.show();
});
