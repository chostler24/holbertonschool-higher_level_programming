-- lists shows in db hbtn_0d_tvshows that have >= 1 genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.show_id=tv_shows.id
ORDER BY tv_shows.title ASC;
