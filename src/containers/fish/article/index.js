/* eslint-env browser */

import 'lazysizes';
import $ from 'jquery';
import ImageGallery from '../../image_gallery';

import '../../../css/fish/article.scss';


$(document).ready(() => {
  $('p:has(img)').addClass('img');

  const iv = new ImageGallery('.article', 'data-src');
  iv.show();
});
