$ = require 'jquery'
key = require 'keymaster'
Editor = require './editor.coffee'
CodeMirror = require 'CodeMirror'
require 'CodeMirror/lib/codemirror.css'
require 'CodeMirror/mode/markdown/markdown.js'
require 'CodeMirror/theme/solarized.css'


editor = new Editor
editor.render()

key 's', editor.save

editorTextarea = document.getElementById('markdown_content')
codeEditor = CodeMirror.fromTextArea(editorTextarea, {
  mode: 'markdown',
  theme: 'solarized',
})

codeEditor.on 'change', (instance, changeObj) ->
  # editorTextarea.value = instance.getValue()
  instance.save()
  editor.render()
