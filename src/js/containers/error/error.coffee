$ = require 'jquery'

$(document).ready ->
  sr.reveal('p', {container: '.top', rotate: {y: 65}, duration: 600})
  sr.reveal('.connect', {container: '.top', rotate: {z: 65}})
  $('html').removeClass('sr')
  return
