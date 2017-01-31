$ = require 'jquery'
# _ = require 'lodash'
key = require 'keymaster'


class ImageView
  constructor: (@selector) ->

  getImages: ->
    images = $(@selector + ' img')
    # imageSrc = _.map(images, (img) ->
    #   img.src
    # )
    return images

  close: ->
    $('body').removeClass('model-open')
    $('.model').removeClass('show')

  show: (childSelector) =>
    $(@selector + ' ' + childSelector).click ->
      $('.model img').remove()
      $('.model').append($(this).clone())

      $('.model').addClass('show')

      $('body').addClass('model-open')
    $('.model .bg').click =>
      @close()
    key 'esc', @close

module.exports = ImageView
