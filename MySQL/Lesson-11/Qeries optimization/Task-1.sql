/* Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
 *catalogs и products в таблицу logs помещается время и дата создания записи, 
 *название таблицы, идентификатор первичного ключа и содержимое поля name. */


use shop;

drop table if exists logs;
create table logs(
record varchar(255)
) comment 'Таблица для логирования' engine=archive;


drop trigger if exists arhcive_users;
drop trigger if exists arhcive_catalogs;
drop trigger if exists arhcive_products;

-- создаем тригерры что бы при каждой вставке в таблицы появлялась соответствующая запись в логе

delimiter //
create trigger arhcive_users before insert on users
for each row
begin
	declare user_id bigint;
	select count(*) + 1 into user_id from users;
	insert into logs values 
	(concat('Время создания: ', now(),'; users; pk_id: ', new.id, '; содержимое name: ', new.name));
end//
create trigger arhcive_catalogs before insert on catalogs
for each row
begin
	insert into logs values 
	(concat('Время создания: ', now(),'; catalogs; pk_id: ', new.id, '; содержимое name: ', new.name));
end//
create trigger arhcive_products before insert on products
for each row
begin
	insert into logs values 
	(concat('Время создания: ', now(),'; products; pk_id: ', new.id, '; содержимое name: ', new.name));
end//
delimiter ;


-- проверяем вставляя новые данные в таблицы
insert into catalogs values (10, 'Блоки питания');
insert into users(id, name) values (7, 'Петя');
insert into products(id, name) values (8, 'Чудо дрын');
