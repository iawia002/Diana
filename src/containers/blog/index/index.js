/* eslint-env browser */

import 'balloon-css/balloon.css';
import 'font-awesome/css/font-awesome.css';
import 'notie/dist/notie.min.css';
import $ from 'jquery';
import notie from 'notie';

import '../common/more';
import utils from '../../utils';
import '../../../css/index.scss';


$(document).ready(() => {
  window.sr.reveal('.article', { reset: true });
  window.sr.reveal('.avatar', { container: '.top', rotate: { x: 65 } });
  window.sr.reveal('h1', { container: '.top', rotate: { y: 65 } });
  window.sr.reveal('.introduction', { container: '.top', rotate: { y: 65 }, duration: 600 });
  window.sr.reveal('.last-article', { container: '.top', rotate: { y: 65 }, duration: 600 });
  window.sr.reveal('.nav', { container: '.top', rotate: { x: 65 } });
  $('html').removeClass('sr');

  $('#introduction span').click(() => {
    const xsrf = utils.getCookie('_xsrf');
    const originIntroduction = $('#introduction p').text();
    notie.input({
      text: 'hello',
      submitText: '更新',
      cancelText: '取消',
      placeholder: originIntroduction,
      submitCallback: (value) => {
        $.post({
          url: '/user',
          data: {
            introduction: value,
            _xsrf: xsrf,
          },
          success: () => {
            notie.alert({ type: 'success', text: 'success' });
            $('#introduction p').text(value);
          },
          error: () => {
            notie.alert({ type: 'error', text: 'error' });
          },
        });
      },
      type: 'text',
    });
  });
});
