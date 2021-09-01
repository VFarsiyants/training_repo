-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
-- Следует учесть, что необходимы дни недели текущего года, а не года рождения.

select count(*), dayname(concat(year(now()), substring(birthday_at, 5))) as dayname_in_current_year  from users
group by dayname_in_current_year;