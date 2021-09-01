-- Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы 
-- типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. 
-- Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.

-- В изначальной таблице нет данной ошибки, поэтому смоделирую ее самостоятельно.
-- для начала копирую структуру таблицы users в users_for_task для нас это будет исходная таблица
drop table users_for_task if exists;
create table users_for_task like users;
-- изменяем типы полей created_at, updated_at тем самым создавая ошибку
alter table users_for_task modify created_at varchar(100);
alter table users_for_task modify updated_at varchar(100);
-- заполняем тпблицу данными по примеру указанному в ПЗ
insert into users_for_task (name, birthday_at, created_at, updated_at) values 
('Vladislav Farsiyants', '1994-09-21', '04.08.2021 10:45', '04.08.2021 10:45'),
('Konstantin Sivakozov', '1993-07-10', '04.08.2021 9:45', '04.08.2021 9:45'),
('Roman Radchenko', '1993-08-24', '03.08.2021 21:45', '03.08.2021 21:45');
-- создаем новую таблицу взамен откорректированной с корректными полями
drop table user_correct if exists;
create table users_correct like users_for_task;
alter table users_correct modify created_at datetime;
alter table users_correct modify updated_at datetime;

-- вставляем в новую таблицу значения из предыдущей используя функцию STR_TO_DATE для конвертации из строки в формат datetime
insert into users_correct (id, name, birthday_at, created_at, updated_at) 
select id, name, birthday_at, STR_TO_DATE(created_at, '%d.%m.%Y %H:%i'), STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i') from users_for_task;

-- удаляем таблицу users_for_task и переименовываем откорректированную таблицу в исходную.
drop table users_for_task;
rename table users_correct to users_for_task;