-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

select id, name
from users u 
where id in (select distinct user_id from orders o);