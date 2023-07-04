select hour(datetime) as hour, 
count(*) as count
from animal_outs
where hour(datetime) between 9 and 20
group by 1
order by 1;