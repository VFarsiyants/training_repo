/*¬ таблице products есть два текстовых пол€: name с названием товара и description с его описанием. 
 * ƒопустимо присутствие обоих полей или одно из них. —итуаци€, когда оба пол€ принимают неопределенное
 *значение NULL неприемлема. »спользу€ триггеры, добейтесь того, чтобы одно из этих полей или оба пол€
 *были заполнены. ѕри попытке присвоить пол€м NULL-значение необходимо отменить операцию. */ 

drop trigger if exists products_check
delimiter //
create trigger products_check before insert on products
for each row begin
	if ((new.name is null) and (new.description is null)) then
		signal sqlstate '45000' set MESSAGE_TEXT = 'INSERT canceled';
	end if;
end //
delimiter ;

insert into products(name, description) values (null, null);