$ = require 'jquery'
hljs = require 'highlight.js'
ImageGallery = require '../common/image_gallery.coffee'

hljs.initHighlightingOnLoad()

$(document).ready ->
  $('p:has(img)').addClass('img')
  $('pre code').each (i, block) ->
    hljs.highlightBlock(block)
    return
  sr.reveal('.article', {viewFactor: 0.000001})
  $('html').removeClass('sr')
  iv = new ImageGallery '.article'
  iv.show('img')
  return
