-- Определить кто больше поставил лайков (всего) - мужчины или женщины?

select concat('больше всего лайков поставили', ' ', gender) result
from (
		-- определяем сколько лайков поставили мужчины
		select count(*) given_likes, 'мужчины' gender from likes l 
		where user_id in (	select user_id 
							from profiles p 
							where gender = 'M')
		union	-- объдиняем результат с числом лайков женщин
		-- определяем сколько лайков поставили женщины
		select count(*) given_likes, 'женщины' gender from likes l 
		where user_id in (	select user_id 
							from profiles p 
							where gender = 'F')
		order by given_likes desc -- сортируем по убыванию берем верхнее значение
		limit 1) as likes_gender