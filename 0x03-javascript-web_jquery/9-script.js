const URL = 'https://stefanbohacek.com/hellosalut/?lang=fr';
$.get(URL, (data) => {
  $('DIV#hello').text(data.hello);
});
