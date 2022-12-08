const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(URL, (data) => {
  $.each(data.results, (char, movie) => {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  });
});
