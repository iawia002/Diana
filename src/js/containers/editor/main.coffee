$ = require 'jquery'
key = require 'keymaster'
Editor = require './editor.coffee'

editor = new Editor

editor.render()

$('#markdown_content').keyup(editor.render)

key 's', editor.save
