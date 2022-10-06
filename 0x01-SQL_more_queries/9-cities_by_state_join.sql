-- list all cities contained in db hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.states_id=states.id
