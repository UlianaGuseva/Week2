-- create table script (
-- movie_id int,
-- title varchar(50),
-- author varchar(50),
-- story text,
-- primary key (movie_id),
-- constraint fk_movie_id foreign key (movie_id) references movies(id)
-- );

-- insert into script (movie_id, title, author, story)
-- values
-- ((select id from movies where title = 'One'), 
--  'one', 
--  'Uliana', 
--  'great story about...')

-- insert into script (movie_id, title, author, story)
-- values
-- ((select id from movies where title = 'Two'),
--  'Two',
--  'Alexander',
--  'the romantic story of...'
-- )
-- update script set title = 'One' where title = 'one'

-- create or replace function full_name(first_name varchar(50), last_name varchar(50))
-- returns varchar(100) as $$
-- 	begin
-- 		return first_name ||' '|| last_name;
-- 	end

-- $$ language plpgsql; -- or Python
-- select * from full_name('Yossi', 'Eik');
-- select full_name (first_name, last_name) from actors;
-- select number_oscars, full_name (first_name, last_name) from actors;

