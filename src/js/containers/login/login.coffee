$ = require 'jquery'

$(document).ready ->
  sr.reveal('.avatar', {rotate: {x: 65}})
  sr.reveal('input', {rotate: {y: 65}, duration: 600})
  sr.reveal('button')
  $('html').removeClass('sr')
  return
