# Write your MySQL query statement below
select u.name as NAME, f.total as BALANCE
from users u
join 
(select account , sum(amount) as total
from transactions
group by account
having sum(amount)>10000) f
on u.account=f.account
