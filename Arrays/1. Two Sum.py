class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i,j in enumerate(nums):
            a=target-j
            if a in nums[i+1:]:
                x.append(nums.index(j))
                x.append(nums.index(target-j,i+1))
                break
        return x

    
    create table TIME(
time_id  varchar(20),
Year varchar(20),
Quarter varchar(20),
Month varchar(20),
Date varchar(20),
Day of Week varchar(20),
Day of Month varchar(20),
Holiday Flag varchar(20)),
constraint time_id_pk primary key(cust_id));

create table PRODUCT(
product_id varchar(20),
type_id varchar(20),
Manufacturing Date varchar(20),
Expiry Date date(20),
Availability varchar(20),
Max Qantity varchar(20)
constraint product_id_pk primary key(product_id));


create TYPE (
type_id varchar(20),
Category varchar(20),
Type varchar(20)
constraint type_id_pk primary key(type_id));


create LOCATION (
location_id varchar(20),
Address varchar(20),
Region varchar(20),
State varchar(20),
City varchar(20)
constraint location_id_pk primary key(location_id));

create STORE (
store_id varchar(20),
Store Name varchar(20),
location_id varchar(20)
constraint store_id_pk primary key(store_id));


create SUPPLIER(
supplier_id varchar(20),
Cost Price varchar(20),
Quantity varchar(20),
Product varchar(20),
Address varchar(20)
constraint supplier_id_pk primary key(supplied_id));
