/*Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу 
 * "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи". */


drop function if exists hello;
delimiter //


create function hello ()
returns text deterministic
begin
	if ((curtime() > '06:00:00') and (curtime() < '12:00:00')) then 
		return 'Доброе утро';
	elseif ((curtime() > '12:00:00') and (curtime() < '18:00:00')) then
		return 'Добрый день';
	elseif ((curtime() > '18:00:00') and (curtime() < '24:00:00')) then
		return 'Добрый вечер';
	else
		return 'Доброй ночи';
	end if;
end//

delimiter ;

-- запрос для проверки работы функции
select hello();