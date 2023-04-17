-- select * from customer;
-- select concat(first_name,' ',last_name) as full_name from customer;
-- select create_date from customer group by create_date;
-- select * from customer order by first_name desc;
-- select film_id, title, description, release_year, rental_rate from film order by rental_rate;
-- select address, phone from address where district = 'Texas';
-- select * from film where film_id = 15 or film_id = 150;
-- select film_id, title, description, length, rental_rate from film where title like 'Har%';
-- select * from film order by rental_rate limit 10;
-- select * from film order by rental_rate limit 10 offset 10;

-- select first_name, last_name, amount, payment_date
-- from customer 
-- join payment 
-- on customer.customer_id = payment.customer_id 
-- order by customer.customer_id;

-- select title, film_id
-- from film where film_id not in (select film_id from inventory)

-- select city, country
-- from city
-- join country
-- on city.country_id = country.country_id


-- select customer.customer_id, first_name, last_name, amount, payment_date, staff_id 
-- from customer
-- join payment
-- on customer.customer_id = payment.customer_id order by staff_id;


