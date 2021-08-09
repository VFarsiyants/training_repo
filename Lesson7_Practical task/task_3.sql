-- (по желанию) ѕусть имеетс€ таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- ѕол€ from, to и label содержат английские названи€ городов, поле name Ч русское. ¬ыведите список рейсов 
-- flights с русскими названи€ми городов.

-- готовим Ѕƒ дл€ выполнени€ задани€
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
-- наполн€ем таблицы данными
insert into flights(`from`, `to`) values
('moscow', 'omsk'),
('novgorod', 'kazan'),
('irkutsk', 'moscow'),
('omsk', 'irkutsk'),
('moscow', 'kazan');

insert into cities(label, name) values
('moscow', 'ћосква'),
('irkutsk', '»ркутск'),
('novgorod', 'Ќовгород'),
('kazan', ' азань'),
('omsk', 'ќмск');
-- пишем наш запрос, нам нужно будет умножить таблицу два раза
select from_c.name, to_c.name from flights f
join cities to_c 
-- первое умножение дл€ опредлени€ соответсви€ куда
on f.`to` = to_c.label
join cities from_c
-- второе умножение дл€ опредлени€ соответсви€ откуда
on f.`from` = from_c.label;

