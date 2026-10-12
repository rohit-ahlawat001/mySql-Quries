# Write a MySQL query to retrieve all columns for employees whose salary is greater than ₹50,000.

select *  from employees where salary > 50000

# Using the same employees table, write a query to retrieve only the employee's name and salary for employees working in the IT department.

select name, salary from employees where department = "IT"


# Using the same employees table, write a query to:
# 1. Retrieve the employee's name and salary.
# 2. Include only employees earning at least ₹40,000.
# 3. Sort the results by salary from highest to lowest.

select name, salary from employees where salary >= 40000 order by salary desc



# Using the same employees table, write a query to retrieve the name, department, and salary of employees who satisfy both conditions:
# 1. Their department is IT.
# 2. Their salary is greater than ₹50,000.


SELECT name, department, salary FROM employees WHERE department = 'IT' AND salary > 50000;



# Using the same employees table, write a query to retrieve the name and department of employees who work in either the HR department or the Finance department.
# Return only name and department. Include employees from both departments. Do not return employees from IT.

select name,department from employees where department = "HR"  or department = "Finance"
