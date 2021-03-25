# Write your MySQL query statement below
select Person.FirstName , Person.LastName , Address.City , Address.State
from person
left join address on Person.PersonId = Address.PersonId
