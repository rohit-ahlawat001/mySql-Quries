# Write a MySQL query to retrieve all columns for employees whose salary is greater than ₹50,000.

select *  from employees where salary > 50000

# Using the same employees table, write a query to retrieve only the employee's name and salary for employees working in the IT department.

select name, salary from employees where department = "IT"