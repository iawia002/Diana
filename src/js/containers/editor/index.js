'use strict';

import 'CodeMirror/lib/codemirror.css';
import 'CodeMirror/mode/gfm/gfm.js';
import 'CodeMirror/theme/solarized.css';

import '../../../css/editor.scss';
import 'font-awesome/css/font-awesome.css';
import 'highlight.js/styles/solarized-dark.css';

import $ from 'jquery';
import key from 'keymaster';
import CodeMirror from 'CodeMirror';
import Editor from './editor.js'


const editor = new Editor();
editor.render();

key('s', editor.save);

const editorTextarea = document.getElementById('markdown_content');
const codeEditor = CodeMirror.fromTextArea(editorTextarea, {
  mode: 'gfm',
  theme: 'solarized',
  lineWrapping: true,
});

codeEditor.on('change', (instance, changeObj) => {
  instance.save();
  editor.render();
});

codeEditor.on('scroll', (instance) => {
  const scrollInfo = instance.getScrollInfo();
  const percentage = (scrollInfo.top + scrollInfo.clientHeight) / scrollInfo.height;
  const outputHeight = $('#output')[0].scrollHeight - $('#output')[0].offsetHeight;
  $('#output').scrollTop(percentage * outputHeight);
});
