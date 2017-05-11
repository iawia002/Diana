import '../css/article.scss';

import 'lazysizes';
import $ from 'jquery';
import ImageGallery from '../../image_gallery.js'


$(document).ready(() => {
  $('p:has(img)').addClass('img');

  const iv = new ImageGallery('.article', 'data-src');
  iv.show();
});
