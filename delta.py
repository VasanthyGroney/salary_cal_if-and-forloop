from employee import employees


def calculate_overtime_pay(hours_worked, hourly_rate):
    """Calculate the overtime pay for an employee."""
    if hours_worked <= 40:
        return 0.0
    else:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        return overtime_pay


def calculate_total_pay(employee):
    """Calculate the total pay for an employee, including overtime."""
    name = employee['name']
    hours_worked = employee['hours_worked']
    hourly_rate = employee['hourly_rate']

    regular_pay = min(hours_worked, 40) * hourly_rate
    overtime_pay = calculate_overtime_pay(hours_worked, hourly_rate)
    total_pay = regular_pay + overtime_pay

    return {
        "name": name,
        "hours_worked": hours_worked,
        "total_pay": round(total_pay, 2)  # Round total pay to 2 decimal places
    }


# Get input from user
input_employee_name = input("Enter Employee Name: ")

# Find the employee record
employee_record = next((emp for emp in employees if emp['name'].lower() == input_employee_name.lower()), None)

if employee_record:
    # Prompt for any additional overtime hours
    extra_hours = int(input(f"Enter any additional overtime hours for {input_employee_name}: "))
    employee_record['hours_worked'] += extra_hours

    # Calculate the total pay
    total_pay_info = calculate_total_pay(employee_record)

    # Print the result
    print(total_pay_info)
else:
    print("Employee not found.")
