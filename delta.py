# hours_worked: The number of hours the employee worked (an integer)
# hourly_rate: The hourly rate of the employee (a float)
# Write a function calculate_overtime_pay(employees) that takes a list of employee records and performs the following tasks:
#
# Calculate the total pay for each employee based on their hours worked and hourly rate:
# For hours up to 40, use the regular hourly rate.
# For hours over 40, calculate overtime pay at 1.5 times the hourly rate for each overtime hour.
# Return a new list of dictionaries where each dictionary contains:
# name: The name of the employee
# hours_worked: The total hours worked by the employee
# total_pay: The total pay for the employee
# Example Input
from employee import employees

def information_employee(employees):
    salary = []
    if input_employee in employees:
        for employee in employees:
            name = employee['name']
            hours_worked = employee['hours_worked']
            hourly_rate = employee['hourly_rate']
            salary = hours_worked * hourly_rate
        return salary

def overtime_salary(extra_hour):
    if input_employee in employees:
        for employee in employees:
            name = employee['name']
            overtime_worked =
            overtime = overtime_worked * hourly_rate
            hourly_rate = employee['hourly_rate']
            salary = hours_worked * hourly_rate
        return salary


input_employee = input("Enter Employee Nmae: ")
overtime = int(input(f"Enter {input_employee} overtime hours: "))



