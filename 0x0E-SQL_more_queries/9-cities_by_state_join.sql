-- 9. Cities by States
-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities
RIGHT JOIN states ON states.id = cities.state_id
