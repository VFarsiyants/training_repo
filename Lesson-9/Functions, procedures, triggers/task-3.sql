/*(по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел.
Вызов функции FIBONACCI(10) должен возвращать число 55.*/

drop function if exists fibonacci;
delimiter //
create function fibonacci (num bigint)
returns bigint deterministic
begin
	declare temp bigint;
	declare p2 bigint default 0;
	declare p1 bigint default 1;
	declare i bigint default 2;
	if num = 0 then 
		return 0;
	elseif num = 1 then
		return 1;
	else
		while (i < num) do
			set temp = p1;
			set p1 = p1 + p2;
			set p2 = temp;
			set i = i + 1;
		end while;
		return p1 + p2;
	end if;
end//
delimiter ;

select fibonacci(10);