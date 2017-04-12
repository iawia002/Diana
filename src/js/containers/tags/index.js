'use strict';

import '../../../css/article.scss';
import 'font-awesome/css/font-awesome.css';

import $ from 'jquery';


$(document).ready(() => {
  sr.reveal('.article', {viewFactor: 0.000001});
  $('html').removeClass('sr');
});
