-- (по желанию) Из таблицы users необходимо извлечь пользователей, 
-- родившихся в августе и мае. Месяцы заданы в виде списка английских названий (may, august)


-- создаем таблицу которую буем использовать для решения задачи

drop table users_for_task_4 if exists

create table users_for_task_4 like users;
alter table users_for_task_4 modify birthday_at varchar(100);
-- заполняем таблицу данными среди которых будем искать пользователей родившихся в в мае и августе
insert into users_for_task_4(name, birthday_at) values
('Vladislav Farsiyants', '21 september 1994'),
('Kostya Sivakozov', '10 july 1993'),
('Roman Radchenko', '24 july 1993'),
('Aksinia Farsiyants', '9 may 1991'),
('Vasya Pupkin', '18 august 1983');

-- выполняем выборки и таблицы с использованием условия с опретором rlike для которого задаем возможные месяцы (august или may)
select*from users_for_task_4 uft 
where birthday_at rlike '.*august|may.*';