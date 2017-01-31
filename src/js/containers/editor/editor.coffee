$ = require 'jquery'
marked = require 'marked'
hljs = require 'highlight.js'
utils = require '../../utils.coffee'


hljs.configure
  tabReplace: '    '

renderer = new marked.Renderer()
marked.setOptions
  renderer: renderer
  gfm: true
  tables: true
  breaks: true
  pedantic: false
  sanitize: false
  smartLists: true
  smartypants: false
  langPrefix: 'hljs '
  highlight: (code, lang) ->
    hljs.highlightAuto(code, [lang]).value


class Editor
  render: ->
    # document.getElementById('output').innerHTML \
      # = marked($('#markdown_content').val())
    $('#output').html(marked($('#markdown_content').val()))

  getTags: ->
    tags = new Array()
    $('ul').last().children('li').each ->
      tags.push($(this).text())
    return tags

  save: =>
    @render()
    tags = JSON.stringify(@getTags())
    $('#output ul').last().remove()
    _xsrf = utils.getCookie('_xsrf')
    $.post
      url: '/p/' + $('#article_id').val() + '/edit'
      data:
        article_id: $('#article_id').val()
        title: $('#output h1').html()
        introduction: if $('#output blockquote').html() \
          then $('#output blockquote').html() else ''
        markdown_content: $('#markdown_content').val()
        compiled_content: $('#output').html()
        tags: tags
        _xsrf: _xsrf
      success: ->
        alert('success')
      error: ->
        alert('error')


module.exports = Editor
