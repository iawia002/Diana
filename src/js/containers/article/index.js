'use strict';

import 'font-awesome/css/font-awesome.css';
import 'highlight.js/styles/solarized-light.css';
import '../../../css/article.scss';

import $ from 'jquery';
import key from 'keymaster';
import Hammer from 'hammerjs';
import hljs from 'highlight.js';
import ImageGallery from '../common/image_gallery.js'

hljs.initHighlightingOnLoad();

$(document).ready(() => {
  $('p:has(img)').addClass('img');
  $('pre code').each((i, block) => {
    hljs.highlightBlock(block);
  });
  sr.reveal('.article', {viewFactor: 0.000001});
  $('html').removeClass('sr');

  const iv = new ImageGallery('.article');

  const stage = document.getElementById('content-model');
  const mc = new Hammer.Manager(stage);
  const SwipeLeft = new Hammer.Swipe({
    event: 'swipeleft',
    direction: Hammer.DIRECTION_LEFT,
  });
  const SwipeRight = new Hammer.Swipe({
    event: 'swiperight',
    direction: Hammer.DIRECTION_RIGHT,
  });
  const Tap = new Hammer.Tap();
  mc.add(SwipeLeft);
  mc.add(SwipeRight);
  mc.add(Tap);

  $('.article img').click((e) => {
    const index = iv.images.indexOf(e.target.src);
    iv.changeImage(index);
    $('.model').addClass('show animated fadeIn');
    setTimeout(() => {
      $('.model').removeClass('animated fadeIn');
    }, 300);
    $('body').addClass('model-open');
  });

  key('right', iv.right);
  // 滑动操作的左右是反的，往左滑是下一张
  mc.on('swiperight', iv.left);
  // 点击显示下一张
  mc.on('tap', iv.right);

  key('left', iv.left);
  mc.on('swipeleft', iv.right);

  $('.model .bg').click(() => {
    iv.close();
  });
  key('esc', iv.close);
});
