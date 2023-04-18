-- create table product_orders (
-- id serial primary key,
-- quantity int not null, 
-- "date" timestamp not null default current_timestamp
-- )

-- alter table product_orders add column customer varchar;

-- create table items (
-- item_id serial primary key,
-- name varchar(50) not null unique,
-- price int,
-- weight float,
-- product_id int references product_orders(id) on delete no action
-- )
-- create table users (
-- user_id serial primary key,
-- name varchar(50) not null unique,
-- price int,
-- weight float,
-- product_id int references product_orders(id) on delete no action
-- )

-- insert into product_orders (quantity, customer)
-- values
-- (5, 'Sam'),
-- (3, 'Tom'),
-- (1, 'Liz'),
-- (2, 'Alex');

-- insert into items (name, price, weight, product_id)
-- values
-- ('a', 50, 300, (select id from product_orders where customer = 'Sam')),
-- ('b', 10, 120, (select id from product_orders where customer = 'Tom')),
-- ('c', 20, 30, (select id from product_orders where customer = 'Tom')),
-- ('d', 5, 60, (select id from product_orders where customer = 'Liz')),
-- ('e', 5, 370, (select id from product_orders where customer = 'Sam')),
-- ('f', 7, 60, (select id from product_orders where customer = 'Tom')),
-- ('g', 13, 20, (select id from product_orders where customer = 'Sam')),
-- ('h', 21, 90, (select id from product_orders where customer = 'Sam')),
-- ('i', 16, 350, (select id from product_orders where customer = 'Sam')),
-- ('j', 57, 300, (select id from product_orders where customer = 'Alex')),
-- ('k', 4, 270, (select id from product_orders where customer = 'Alex'));


-- create or replace function order_price (order_id int)
-- returns int as $$
-- 	declare 
-- 	total_sum int;
-- 	begin
-- 		total_sum := (select sum(price) from items
-- 			join product_orders
-- 			on
-- 			product_orders.id = items.product_id
-- 			where product_orders.id = order_id);
-- 		return total_sum;
-- 	end;
	
-- $$ language plpgsql;

-- select * from order_price(1);
-- select * from order_price(2);
-- select * from order_price(3);
-- select * from order_price(4);





