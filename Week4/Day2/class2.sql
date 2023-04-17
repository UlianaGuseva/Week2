-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Angelina ','Jolie ','04/06/1975', 1);


-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Scarlett','Johansson ','22/11/1984', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Johnny','Depp ','09/06/1963', 3),
-- ('George','Clooney ','05/06/1961', 2),
-- ('Brad','Pitt ','18/12/1963', 2);

-- alter table actors rename column age to birthday

-- alter table actors
-- alter column number_oscars
-- set data type bigint;

-- person - id
-- car - owner_id(person_id)

-- create table apartment (
-- id serial primary key,
-- location varchar(50),
-- actor_id int references actors(actor_id)
-- );
-- -- fkey - foreign key

-- insert into  apartment (location, actor_id)
-- values
-- ('bev hills', 1);

-- insert into  apartment (location, actor_id)
-- values
-- ('Afula', (select actor_id from actors where first_name = 'Brad'));

-- select first_name, last_name, location
-- from actors
-- join apartment
-- on actors.actor_id = apartment.actor_id;
-- --  inner join

-- create table producers(
-- prod_id serial primary key,
-- prod_name varchar
-- );

-- insert into producers (prod_name)
-- values 
-- ('Tim Berton'),
-- ('Alfonso Kuaron'),
-- ('Piter Funk');

-- alter table apartment rename column actor_id to master_id;

-- select prod_name, location
-- from producers
-- join apartment
-- on producers.prod_id = apartment.master_id;

-- alter table apartment add column prod_id int;
-- alter table apartment add constraint fk_producers
-- foreign key (prod_id) references producers(prod_id);

-- select prod_name, location
-- from producers
-- left join apartment
-- on producers.prod_id = apartment.prod_id;

-- one to many relationship 
-- one actor can have many apartments, and one apartment can have just one actor

-- insert into apartment (location, actor_id) 
-- values
-- ('Alaska', (select id from actors where first_name = 'Tina'));


-- many to many
-- one actor can play in many movies, and one movie can include many actors

-- actors -> actors_movies <- movies

-- create table movies (
-- id serial primary key,
-- title varchar(50)
-- ); 


-- create table actors_movies (
-- actor_id int references actors(actor_id),
-- movie_id int references movies(id)
-- ); 


-- insert into movies (title) values 
-- ('Pulp fiction');


-- insert into actors_movies (actor_id, movie_id) values
-- ((select actor_id from actors where first_name = 'Angelina'), (select id from movies where title = 'Pulp fiction')),
-- ((select actor_id from actors where first_name = 'Brad'), (select id from movies where title = 'Pulp fiction')),
-- ((select actor_id from actors where first_name = 'Matt'), (select id from movies where title = 'Pulp fiction'));


-- insert multiple movies for same actor 
-- insert into movies (title) values 
-- ('One'),
-- ('Two'),
-- ('Three');

-- insert into actors (first_name, last_name, birthday, number_oscars) values 
-- ('Main', 'Actor', '1980-01-01', 1);

insert into actors_movies (actor_id, movie_id) values
((select actor_id from actors where first_name = 'Main'), (select id from movies where title = 'One')),
((select actor_id from actors where first_name = 'Main'), (select id from movies where title = 'Two')),
((select actor_id from actors where first_name = 'Main'), (select id from movies where title = 'Three'));
