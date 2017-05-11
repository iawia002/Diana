'use strict';

import $ from 'jquery';
import key from 'keymaster';
import Hammer from 'hammerjs';


export default class ImageGallery {
  constructor(selector, imgSrcAttr) {
    this.selector = selector;
    this.imgSrcAttr = imgSrcAttr;
    this.imageSelector = $(`${this.selector} img`);
    this.images = this.getImages();
    this.left = this.left.bind(this);
    this.right = this.right.bind(this);
  }

  getImages() {
    const self = this;
    const imageSrc = Array();
    self.imageSelector.map((index, element) => {
      imageSrc.push($(element).attr(self.imgSrcAttr));
    });
    return imageSrc;
  }

  changeImage(index) {
    const self = this;
    const imageSrc = self.images[index];
    $('.model .content img')[0].src = imageSrc;
    $('.model .content img').attr('data-id', index);
    $('.model .content p').html(index + 1 + ' / ' + self.images.length);
    $('.model .content a')[0].href = imageSrc;
  }

  right() {
    const self = this;
    const index = $('.model .content img').attr('data-id');
    const nextIndex = (parseInt(index) + 1) % self.images.length;
    self.changeImage(nextIndex);
  }

  left() {
    const self = this;
    const index = $('.model .content img').attr('data-id');
    let nextIndex = parseInt(index) - 1;
    if (nextIndex < 0) {
      nextIndex = self.images.length - 1;
    }
    self.changeImage(nextIndex);
  }

  close() {
    $('.model').addClass('animated fadeOut');
    $('body').removeClass('model-open');
    setTimeout(() => {
      $('.model').removeClass('show animated fadeOut');
    }, 300);
  }

  show() {
    const self = this;
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

    self.imageSelector.click((e) => {
      const index = self.images.indexOf(e.target.src);
      self.changeImage(index);
      $('.model').addClass('show animated fadeIn');
      setTimeout(() => {
        $('.model').removeClass('animated fadeIn');
      }, 300);
      $('body').addClass('model-open');
    });

    key('right', self.right);
    // 滑动操作的左右是反的，往左滑是下一张
    mc.on('swiperight', self.left);
    // 点击显示下一张
    mc.on('tap', self.right);

    key('left', self.left);
    mc.on('swipeleft', self.right);

    $('.model .bg').click(() => {
      self.close();
    });
    key('esc', self.close);
  }
}
