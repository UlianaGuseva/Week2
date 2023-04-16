-- create table students (
-- id serial primary key,
-- last_name varchar,
-- first_name varchar,
-- birth_date date
-- );

-- insert into students(last_name, first_name, birth_date)
-- values 
-- ('Benichou', 'Marc', '1998-11-02'),
-- ( 'Cohen', 'Yoan','2010-12-03'),
-- ('Benichou', 'Lea', '1987-07-27'),
-- ('Dux', 'Amelia', '1996-04-07'),
-- ('Grez', 'David', '2003-06-14'),
-- ('Simpson', 'Omer', '1980-10-03');

-- insert into students(last_name, first_name, birth_date)
-- values 
-- ('Guseva', 'Uliana', '1994-03-12')

-- select first_name, last_name from students where id = 2;
-- select first_name, last_name from students where first_name = 'Marc' and last_name = 'Benichou';
-- select first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou';
-- select first_name, last_name from students where first_name like '%a%';
-- select first_name, last_name from students where first_name like 'a%';
-- select first_name, last_name from students where first_name like '%a';
-- select first_name, last_name from students where first_name like '%a_';
-- select first_name, last_name from students where id = 1 or id = 3;
select * from students where birth_date <= '2000-01-01';




