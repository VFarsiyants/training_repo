-- (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов 
-- flights с русскими названиями городов.

-- готовим БД для выполнения задания
drop table if exists lesson_7_pz;
create database lesson_7_pz;
-- создаем таблицы согласно заданию
drop table if exists flights;
create table flights(
id serial primary key,
`from` varchar(100),
`to` varchar(100)
);

drop table if exists cities;
create table cities(
label varchar(100),
name varchar(100)
);
-- наполняем таблицы данными
insert into flights(`from`, `to`) values
('moscow', 'omsk'),
('novgorod', 'kazan'),
('irkutsk', 'moscow'),
('omsk', 'irkutsk'),
('moscow', 'kazan');

insert into cities(label, name) values
('moscow', 'Москва'),
('irkutsk', 'Иркутск'),
('novgorod', 'Новгород'),
('kazan', 'Казань'),
('omsk', 'Омск');
-- пишем наш запрос, нам нужно будет умножить таблицу два раза
select from_c.name, to_c.name from flights f
join cities to_c 
-- первое умножение для опредления соответсвия куда
on f.`to` = to_c.label
join cities from_c
-- второе умножение для опредления соответсвия откуда
on f.`from` = from_c.label;