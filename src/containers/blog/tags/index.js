/* eslint-env browser */

import $ from 'jquery';

import 'font-awesome/css/font-awesome.css';
import '../../../css/blog/article.scss';


$(document).ready(() => {
  window.sr.reveal('.article', { viewFactor: 0.000001 });
  $('html').removeClass('sr');
});
