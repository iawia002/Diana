import $ from 'jquery';

import 'font-awesome/css/font-awesome.css';
import 'src/css/blog/article.scss';

import 'src/containers/blog/common/more';


$(document).ready(() => {
  window.sr.reveal('.article', { reset: true });
  window.sr.reveal('.footer', { reset: true });
  $('html').removeClass('sr');
});
