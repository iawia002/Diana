/* eslint-env browser */

import $ from 'jquery';

import 'font-awesome/css/font-awesome.css';
import '../../../css/blog/article.scss';

import '../common/more';


$(document).ready(() => {
  window.sr.reveal('.article', { reset: true });
  window.sr.reveal('.footer', { reset: true });
  $('html').removeClass('sr');
});
