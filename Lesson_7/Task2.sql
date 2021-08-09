-- Выведите список товаров products и разделов catalogs, который соответствует товару.

select p.name, c.name from products p 
join catalogs c 
on p.catalog_id = c.id 