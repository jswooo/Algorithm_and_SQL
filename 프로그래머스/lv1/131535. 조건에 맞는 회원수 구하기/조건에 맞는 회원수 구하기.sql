select count(user_id) USERS
from user_info
where 20 <= age and age <= 29 and year(joined) = 2021;