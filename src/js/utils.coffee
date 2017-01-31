getCookie = (name) ->
  r = document.cookie.match('\\b' + name + '=([^;]*)\\b')
  if r then r[1] else undefined

module.exports.getCookie = getCookie
