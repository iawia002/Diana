$ = require 'jquery'

$.fn.extend
  animateCss: (animationName) ->
    animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd
      oanimationend animationend'
    @.addClass('animated ' + animationName).one(animationEnd, ->
      $(this).removeClass('animated ' + animationName)
    )
