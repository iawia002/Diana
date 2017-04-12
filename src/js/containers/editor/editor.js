'use strict';

import $ from 'jquery';
import marked from 'marked';
import hljs from 'highlight.js';
import utils from '../../utils.js';


hljs.configure({
  tabReplace: '    ',
});

const renderer = new marked.Renderer();
marked.setOptions({
  renderer: renderer,
  gfm: true,
  tables: true,
  breaks: true,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  langPrefix: 'hljs ',
  highlight: (code, lang) => {
    return hljs.highlightAuto(code, [lang]).value;
  }
});


export default class Editor {
  constructor() {
    this.save = this.save.bind(this); // 防止别的方法来调这个函数时 this 会出错
  }

  render() {
    $('#output').html(marked($('#markdown_content').val()));
  }

  getTags() {
    const tags = new Array();
    $('ul').last().children('li').each((index, element) => {
      tags.push($(element).text());
    });
    return tags;
  }

  save() {
    const self = this;
    self.render();
    const tags = self.getTags();
    $('#output ul').last().remove();
    const _xsrf = utils.getCookie('_xsrf');
    const article_id = $('#article_id').val();
    $.post({
      url: `/p/${article_id}/edit`,
      data: {
        article_id: article_id,
        title: $('#output h1').html(),
        introduction: $('#output blockquote').html() ? $('#output blockquote').html() : '',
        markdown_content: $('#markdown_content').val(),
        compiled_content: $('#output').html(),
        tags: tags,
        _xsrf: _xsrf,
      },
      success: () => {
        alert('success');
      },
      error: () => {
        alert('error');
      }
    });
  }
}
