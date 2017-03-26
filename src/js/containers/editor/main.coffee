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
  lineWrapping: true,
})

codeEditor.on 'change', (instance, changeObj) ->
  # editorTextarea.value = instance.getValue()
  instance.save()
  editor.render()

codeEditor.on 'scroll', (instance) ->
  scrollInfo = instance.getScrollInfo()
  percentage = (scrollInfo.top + scrollInfo.clientHeight) / scrollInfo.height
  outputHeight = $('#output')[0].scrollHeight - $('#output')[0].offsetHeight
  $('#output').scrollTop(percentage * outputHeight)
