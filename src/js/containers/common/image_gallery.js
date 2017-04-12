'use strict';

import $ from 'jquery';

export default class ImageGallery {
  constructor(selector) {
    this.selector = selector;
    this.images = this.getImages();
    this.left = this.left.bind(this);
    this.right = this.right.bind(this);
  }

  getImages() {
    const images = $(`${this.selector} img`);
    const imageSrc = Array();
    images.map((index, element) => {
      imageSrc.push(element.src);
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
}
