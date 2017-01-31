$ = require 'jquery'

$(document).ready ->
  sr.reveal('.article', {reset: true})
  sr.reveal('.avatar', {container: '.top', rotate: {x: 65}})
  sr.reveal('h1', {container: '.top', rotate: {y: 65}})
  sr.reveal('p', {container: '.top', rotate: {y: 65}, duration: 600})
  sr.reveal('.connect', {container: '.top', rotate: {z: 65}})
  $('html').removeClass('sr')
  return
