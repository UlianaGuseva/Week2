-- create table customer (
-- id serial primary key,
-- first_name varchar not null,
-- last_name varchar not null
-- )

-- create table customer_profile (
-- id serial primary key,
-- isloggedin boolean default false,
-- customer_id int references customer(id) on delete cascade
-- );

-- insert into customer (first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- insert into customer_profile (customer_id, isloggedin)
-- values
-- ((select id from customer where first_name = 'John'), true),
-- ((select id from customer where first_name = 'Jerome'), default);

-- select first_name from customer
-- join customer_profile
-- on customer_profile.customer_id = customer.id
-- where isloggedin = true;

--
-- select first_name, customer_id from customer
-- join customer_profile
-- on customer_profile.customer_id = customer.id;

-- select first_name, customer_id, isloggedin from customer
-- left join customer_profile
-- on customer_profile.customer_id = customer.id;

-- select count(isloggedin) from customer_profile;

-- create table book (
-- book_id serial primary key,
-- title varchar not null,
-- author varchar not null
-- )

-- insert into book (title, author)
-- values 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student (
-- student_id serial primary key,
-- name varchar not null unique,
-- age int
-- );

-- insert into student (name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library (
-- book_fk_id int references book(book_id) on delete cascade on update cascade,
-- student_id int references student(student_id) on delete cascade on update cascade,
-- borrowed_date date,
-- primary key (book_fk_id, student_id)
-- )

-- insert into library (book_fk_id, student_id, borrowed_date)
-- values
-- ((select book_id from book where title = 'Alice In Wonderland'), (select student_id from student where name = 'John'), '2022-02-15'),
-- ((select book_id from book where title = 'To kill a mockingbird'), (select student_id from student where name = 'Bob'), '2021-03-03'),
-- ((select book_id from book where title = 'Alice In Wonderland'), (select student_id from student where name = 'Lera'), '2021-05-23'),
-- ((select book_id from book where title = 'Harry Potter'), (select student_id from student where name = 'Bob'), '2021-08-12');

-- select * from library

-- select title, name from student 
-- join library
-- on student.student_id = library.student_id
-- join book
-- on book.book_id = library.book_fk_id

-- select avg(age) from student where name in (
-- select name from student 
-- join library
-- on student.student_id = library.student_id
-- join book
-- on book.book_id = library.book_fk_id 
-- where title = 'Alice In Wonderland')

-- delete from student where name = 'Bob'




