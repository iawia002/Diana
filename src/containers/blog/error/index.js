/* eslint-env browser */

import $ from 'jquery';

import 'balloon-css/balloon.css';
import 'font-awesome/css/font-awesome.css';
import '../../../css/blog/index.scss';


$(document).ready(() => {
  window.sr.reveal('p', { container: '.top', rotate: { y: 65 }, duration: 600 });
  window.sr.reveal('.connect', { container: '.top', rotate: { z: 65 } });
  $('html').removeClass('sr');
});
