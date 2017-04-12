'use strict';

import '../../../css/index.scss';
import 'balloon-css/balloon.css';
import 'font-awesome/css/font-awesome.css';

import $ from 'jquery';


$(document).ready(() => {
  sr.reveal('p', {container: '.top', rotate: {y: 65}, duration: 600});
  sr.reveal('.connect', {container: '.top', rotate: {z: 65}});
  $('html').removeClass('sr');
});
