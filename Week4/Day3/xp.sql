-- select name from language where language_id in (select language_id from film)

-- select title, description, name from film
-- left join language
-- on language.language_id = film.language_id

-- select name from language

-- create table new_film (
-- id serial primary key,
-- name varchar
-- )

-- insert into new_film (name)
-- values
-- ('Avatar'),
-- ('Star Wars'),
-- ('Titanic'),
-- ('Hatico');

-- create table customer_review (
-- review_id serial primary key not null,
-- film_id int references new_film(id) on delete cascade,
-- language_id int references language(language_id),
-- title varchar, 
-- score int,
-- review_text text,
-- last_update timestamp not null default CURRENT_TIMESTAMP
-- )

-- insert into customer_review (film_id, language_id, title, score, review_text)
-- values
-- ((select id from new_film where name = 'Avatar'), (select language_id from language where name = 'English'), 'best film ever', 10, 'text text text...'),
-- ((select id from new_film where name = 'Star Wars'), (select language_id from language where name = 'English'), 'The may of 4th', 10, 'text text text...');

-- delete from new_film where name = 'Avatar'

-- select * from customer_review

-- update film set language_id = (select language_id from language where name = 'Italian') where film_id = 2 or film_id = 4;

-- drop table customer_review

-- select rental.* from film
-- join inventory
-- on film.film_id = inventory.film_id
-- join rental
-- on rental.inventory_id = inventory.inventory_id
-- where return_date is null
-- order by rental_rate desc limit 30;

-- select title, category.name from film 
-- join film_actor
-- on film.film_id = film_actor.film_id
-- join actor
-- on actor.actor_id = film_actor.actor_id
-- join film_category
-- on film_category.film_id = film.film_id
-- join category
-- on category.category_id = film_category.category_id
-- where category.name = 'Sports' and actor.first_name = 'Penelope' and last_name = 'Monroe'

-- select title, length, rating, category.name from film
-- join film_category
-- on film_category.film_id = film.film_id
-- join category
-- on category.category_id = film_category.category_id
-- where length < 60 and rating = 'R' and category.name = 'Documentary'

-- select title from film
-- join inventory
-- on inventory.film_id = film.film_id
-- join rental
-- on rental.inventory_id = inventory.inventory_id
-- join payment
-- on payment.rental_id = rental.rental_id
-- join customer
-- on customer.customer_id = payment.customer_id
-- where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and payment.amount > 4 and return_date > '2005-07-28' and return_date < '2005-08-01' 

-- select title, description, payment.amount from film
-- join inventory
-- on inventory.film_id = film.film_id
-- join rental
-- on rental.inventory_id = inventory.inventory_id
-- join payment
-- on payment.rental_id = rental.rental_id
-- join customer
-- on customer.customer_id = payment.customer_id
-- where film.title like '%Boat%' or film.description like '%Boat%' and customer.first_name = 'Matthew' and customer.last_name = 'Mahan' order by payment.amount desc





