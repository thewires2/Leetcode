# Write your MySQL query statement below
 with cte as (select if(operation ="Sell", price, -1*price) as op_type, stock_name
from stocks)
select  stock_name, sum(op_type) as capital_gain_loss
from cte
group by stock_name
