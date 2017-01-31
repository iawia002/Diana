$ = require 'jquery'

$(document).ready ->
  master = "markdown_content"
  slave = "output"

  sync = ->
    if($(this).attr('id') == slave)
      master_tmp = master
      slave_tmp = slave
      master = slave
      slave = master_tmp

    $("#" + slave).unbind("scroll")

    percentage = this.scrollTop / (this.scrollHeight - this.offsetHeight)

    x = percentage * ($("#" + slave).get(0).scrollHeight \
      - $("#" + slave).get(0).offsetHeight)

    $("#" + slave).scrollTop(x)

    if(typeof(timer) != 'undefind')
      clearTimeout(timer)

    timer = setTimeout(
      ->
        $('#' + slave).scroll sync
        return
      , 200
    )

  $('#' + master + ', #' + slave).scroll(sync)
  return
