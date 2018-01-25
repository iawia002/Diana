import $ from 'jquery';

import 'font-awesome/css/font-awesome.css';
import 'src/css/blog/article.scss';


$(document).ready(() => {
  window.sr.reveal('.article', { viewFactor: 0.000001 });
  $('html').removeClass('sr');
});
