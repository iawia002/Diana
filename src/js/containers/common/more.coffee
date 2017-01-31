$ = require 'jquery'

more = (next_page, page, tag) ->
  $.ajax
    url: '/more'
    method: 'GET'
    data:
      'next_page': next_page
      'page': page
      'tag': tag
    success: (data) ->
      if data
        if page == 'index'
          $('.content').append(data['data'])
        else if page == 'tag'
          $('.left').append(data['data'])
        $('#next_page').val(data['next_page'])
        return
  return

$(window).scroll ->
  scrollTop = $(this).scrollTop()
  scrollHeight = $(document).height()
  windowHeight = $(this).height()
  if scrollTop + windowHeight == scrollHeight
    more(
      $('#next_page').val()
      $('#page').val()
      $('#tag').val()
    )
  return

module.exports = more
