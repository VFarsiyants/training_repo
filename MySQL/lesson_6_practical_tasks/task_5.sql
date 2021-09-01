-- Ќайти 10 пользователей, которые про€вл€ют наименьшую активность в использовании социальной сети.


-- примем паттерн что пользователь хот€ бы один раз выкладывает медиа-контент дл€ профил€
-- индекс активности пользовател€ будем считать суммой общего числа сообщений, медиа-контента, лайков пользовател€, участи€ в сообществах, 
-- создани€ и участи€ в сообществах, отправки запросов на дружбу, далее объедин€ем все запросы и группируем по пользовател€м
-- данное кол-во будем определ€ть по тому, сколько раз пользователь отпрвл€л сообщени€, ставил лайки, загружал контент и тд

select firstname, lastname from users
where id in (select user_id from (
									select count(*) activity, user_id from (
															select admin_user user_id from communities c
															union all
															select initiator_user_id user_id from friend_requests fr 
															union all
															select user_id from media m 
															union all
															select from_user_id user_id from messages m
															union all
															select user_id from likes
															union all
															select user_id from users_comunities uc
														) as activity_index
									group by user_id
									order by activity
									limit 10) as ten_users_with_smalest_activity)
									
-- решение не учитывает пользователей у которых вообще нет никаких сообщений, фото и т.д., т.е с 0ой активностью