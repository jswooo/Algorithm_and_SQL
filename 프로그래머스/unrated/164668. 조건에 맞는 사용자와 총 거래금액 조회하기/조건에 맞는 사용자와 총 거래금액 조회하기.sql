select b.writer_id as user_id, u.nickname, sum(price) as price 
from used_goods_board b inner join used_goods_user u 
on b.writer_id = u.user_id 
where b.status = 'DONE'
group by b.writer_id
having sum(price) >= 700000
order by 3;