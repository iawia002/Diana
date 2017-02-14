$ = require 'jquery'
map = require 'lodash.map'
key = require 'keymaster'
Hammer = require 'hammerjs'


class ImageGallery
  constructor: (@selector) ->

  getImages: ->
    images = $(@selector + ' img')
    imageSrc = map(images, (img) ->
      img.src
    )
    return imageSrc

  @changeImage: (images, index) ->
    imageSrc = images[index]
    $('.model .content img')[0].src = imageSrc
    $('.model .content img').attr('data-id', index)
    $('.model .content p').html(index + 1 + ' / ' + images.length)
    $('.model .content a')[0].href = imageSrc

  close: ->
    $('.model').addClass('animated fadeOut')
    $('body').removeClass('model-open')
    setTimeout(
      ->
        $('.model').removeClass('show animated fadeOut')
      , 300
    )

  show: (childSelector) ->
    stage = document.getElementById('content-model')
    mc = new Hammer.Manager(stage)
    SwipeLeft = new Hammer.Swipe({
      event: 'swipeleft',
      direction: Hammer.DIRECTION_LEFT,
    })
    SwipeRight = new Hammer.Swipe({
      event: 'swiperight',
      direction: Hammer.DIRECTION_RIGHT,
    })
    Tap = new Hammer.Tap()
    mc.add(SwipeLeft)
    mc.add(SwipeRight)
    mc.add(Tap)

    images = @getImages()

    $(@selector + ' ' + childSelector).click ->
      index = images.indexOf(@.src)
      ImageGallery.changeImage(images, index)
      $('.model').addClass('show animated fadeIn')
      setTimeout(
        ->
          $('.model').removeClass('animated fadeIn')
        , 300
      )
      $('body').addClass('model-open')

    right = ->
      index = $('.model .content img').attr('data-id')
      nextIndex = (parseInt(index) + 1) % images.length
      ImageGallery.changeImage(images, nextIndex)

    left = ->
      index = $('.model .content img').attr('data-id')
      nextIndex = parseInt(index) - 1
      if nextIndex < 0
        nextIndex = images.length - 1
      ImageGallery.changeImage(images, nextIndex)

    key 'right', right
    # 滑动操作的左右是反的，往左滑是下一张
    mc.on 'swiperight', left
    # 点击显示下一张
    mc.on 'tap', right

    key 'left', left
    mc.on 'swipeleft', right

    $('.model .bg').click =>
      @close()
    key 'esc', @close

module.exports = ImageGallery
