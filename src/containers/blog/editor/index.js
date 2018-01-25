import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/solarized.css';

import 'font-awesome/css/font-awesome.css';
import 'highlight.js/styles/solarized-dark.css';

import 'src/css/blog/editor.scss';

import $ from 'jquery';
import key from 'keymaster';
import CodeMirror from 'codemirror';
import 'codemirror/mode/gfm/gfm';

import Editor from 'src/containers/blog/editor/editor';


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
  let percentage = 0;
  if (scrollInfo.top !== 0) {
    percentage = (scrollInfo.top + scrollInfo.clientHeight) / scrollInfo.height;
  }
  const outputHeight = $('#output')[0].scrollHeight - $('#output')[0].offsetHeight;
  $('#output').scrollTop(percentage * outputHeight);
});
