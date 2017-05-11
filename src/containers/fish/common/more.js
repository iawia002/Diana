import $ from 'jquery';

const more = (next_page) => {
  $.ajax({
    url: '/fish/more',
    method: 'GET',
    data: {
      'next_page': next_page,
    },
    success: (data) => {
      if (data) {
        $('.main').append(data['data'])
        $('#next_page').val(data['next_page'])
      }
    }
  });
}

$(window).scroll(() => {
  const scrollTop = $(window).scrollTop();
  const scrollHeight = $(document).height();
  const windowHeight = $(window).height();
  if (scrollTop + windowHeight === scrollHeight) {
    more(
      $('#next_page').val()
    );
  }
});
