-- ѕодсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

-- определ€ем лайки принадлежащие медиа 10ти самых юных пользователей
select count(*) likes_received from likes l 
where media_id in (	-- определ€ем media принадлежащее самым юным пользовател€м
					select id from media m 
					where user_id in 	(	-- mysql не позвол€ет использовать limit в подзапросе поэтому така€ странна€ конструкци€
											select user_id from (	-- определ€ем самых молодых пользователей
																select user_id 
																from profiles p 
																order by timestampdiff(year, birthday, now())
																limit 10) as youngest_users))