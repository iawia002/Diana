/* eslint-env browser */

import $ from 'jquery';
import hljs from 'highlight.js';

import 'font-awesome/css/font-awesome.css';
import 'highlight.js/styles/solarized-light.css';
import '../../../css/blog/article.scss';

import ImageGallery from '../../image_gallery';


hljs.initHighlightingOnLoad();

$(document).ready(() => {
  $('p:has(img)').addClass('img');
  $('pre code').each((i, block) => {
    hljs.highlightBlock(block);
  });
  window.sr.reveal('.article', { viewFactor: 0.000001 });
  $('html').removeClass('sr');

  const iv = new ImageGallery('.article', 'src');
  iv.show();
});
