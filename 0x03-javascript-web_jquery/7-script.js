const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(URL, (data) => {
  const uname = data.uname;
  $('DIV#character').text(uname);
});
