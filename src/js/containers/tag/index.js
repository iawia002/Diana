'use strict';

import '../common/more.js';

import '../../../css/article.scss';
import 'font-awesome/css/font-awesome.css';

import $ from 'jquery';


$(document).ready(() => {
  sr.reveal('.article', {reset: true});
  $('html').removeClass('sr');
});
