select month, car_id, records
from (select 
            month(start_date) as month
            , car_id
            , count(start_date) as records
            , sum(count(start_date)) over(partition by car_id) as records_sum
        from 
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where 
            start_date >= '2022-08-01' and start_date < '2022-11-01'
        group by 
            1, 2
        ) as temp 
where records_sum >= 5 
order by month, car_id desc;