$ = require 'jquery'
key = require 'keymaster'
Editor = require './editor.coffee'

editor = new Editor

editor.render()

$('#markdown_content').bind('input propertychange', editor.render)

key 's', editor.save
