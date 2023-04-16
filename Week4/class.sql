-- create table house_expenses (
-- id serial primary key,
-- pay_date date,
-- electricity float,
-- water float,
-- paid_by varchar(10)
-- );

-- insert into house_expenses(pay_date, electricity, water, paid_by)
-- values 
-- ('2023-01-01', 44.4, 14.3, 'Bar'),
-- ('2023-02-01', 44.3, 13.3, 'Yossi'),
-- ('2023-03-01', 44.5, 12.3, 'Shmulik'),
-- ('2023-04-01', 44.1, 16.3, 'Yossi'),
-- ('2023-05-01', 44.2, 15.3, 'Shmulik');

-- select * from house_expenses;

-- select paid_by from house_expenses;

-- select water, electricity from house_expenses;

-- select * from house_expenses where id <= 2;
-- select paid_by from house_expenses where id <= 2;

-- <=
-- <
-- >
-- >=
-- =
-- !=

-- or, and

-- select * from house_expenses where id = 1 or id = 5;
-- select * from house_expenses where id = 1 and paid_by = 'Shmulik';

-- max 
-- min
-- avg
-- sum

-- select min(electricity) from house_expenses;
-- select max(electricity) as max_electricity from house_expenses;
-- select avg(electricity) as avg_electricity from house_expenses where paid_by != 'Yossi';
-- select min(water) as min_water, max(electricity) as max_electricity from house_expenses;

-- select paid_by, avg(electricity) from house_expenses group by paid_by;


-- select paid_by, sum(electricity + water) from house_expenses group by paid_by;
-- select paid_by, max(electricity+water) from house_expenses group by paid_by;

-- update house_expenses set paid_by = 'Bar' where id = 1;
-- update house_expenses set electricity = 0 where paid_by = 'Bar';

-- delete from house_expenses where id = 3;

-- delete from house_expenses where electricity < 44.2;

delete from house_expenses where pay_date > '2023-03-01';
