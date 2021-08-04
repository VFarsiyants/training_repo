-- Подсчитайте средний возраст пользователей в таблице users.

select avg(TIMESTAMPDIFF(year, birthday_at, now())) from users;