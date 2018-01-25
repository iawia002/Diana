import $ from 'jquery';

import 'font-awesome/css/font-awesome.css';
import 'src/css/auth/login.scss';


$(document).ready(() => {
  window.sr.reveal('.avatar', { rotate: { x: 65 } });
  window.sr.reveal('input', { rotate: { y: 65 }, duration: 600 });
  window.sr.reveal('button');
  $('html').removeClass('sr');
});
