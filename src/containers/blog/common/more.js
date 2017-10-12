/* eslint-env browser */

import $ from 'jquery';


const more = (nextPage, page, tag) => {
  $.ajax({
    url: '/more',
    method: 'GET',
    data: {
      next_page: nextPage,
      page,
      tag,
    },
    success: (data) => {
      if (data) {
        if (page === 'index') {
          $('.content').append(data.data);
        } else if (page === 'tag') {
          $('.left').append(data.data);
        }
        $('#next_page').val(data.next_page);
      }
    },
  });
};

$(window).scroll(() => {
  const scrollTop = $(window).scrollTop();
  const scrollHeight = $(document).height();
  const windowHeight = $(window).height();
  if (scrollTop + windowHeight === scrollHeight) {
    more(
      $('#next_page').val(),
      $('#page').val(),
      $('#tag').val(),
    );
  }
});
