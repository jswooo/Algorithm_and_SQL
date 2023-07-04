with recursive cte as (
select 0 as hour 
union all
select hour+1 
    from cte 
    where hour < 23)

select cte.hour as hour, 0
from cte
where cte.hour not in 
(select hour(datetime) from animal_outs
group by hour(datetime))
union all
select hour(datetime) as hour, count(*) as count
from animal_outs
group by 1
order by 1;
