-- Создайте представление, которое выводит название name товарной позиции из 
-- таблицы products и соответствующее название каталога name из таблицы catalogs.


use shop;

create view name_catalog as 
select p.name product_name, c.name catalog_name from products p 
join catalogs c on c.id = p.catalog_id;

select*from name_catalog;
