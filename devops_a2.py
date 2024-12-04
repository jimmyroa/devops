# Adjusted version for non-interactive testing

# CONSTANTS:
FIXED_INCOME_TAX = 18  # Percentage %
CHEF_HOURLY_RATE = 30
WAITER_HOURLY_RATE = 28
DELIVERY_HOURLY_RATE = 25
CLEANER_HOURLY_RATE = 24


# METHODS DEFINITION:
def validate_employee_position_and_calculate(employee_position, employee_monthly_hours):
    if employee_position.lower() == 'chef':
        result = calculate_net_monthly_employee_income(CHEF_HOURLY_RATE, employee_monthly_hours)
        return f"{employee_position.upper()}\nNet monthly income: {result}"

    elif employee_position.lower() == 'waiter':
        result = calculate_net_monthly_employee_income(WAITER_HOURLY_RATE, employee_monthly_hours)
        return f"{employee_position.upper()}\nNet monthly income: {result}"

    elif employee_position.lower() == 'delivery':
        result = calculate_net_monthly_employee_income(DELIVERY_HOURLY_RATE, employee_monthly_hours)
        return f"{employee_position.upper()}\nNet monthly income: {result}"

    elif employee_position.lower() == 'cleaner':
        result = calculate_net_monthly_employee_income(CLEANER_HOURLY_RATE, employee_monthly_hours)
        return f"{employee_position.upper()}\nNet monthly income: {result}"

    else:
        return "Invalid input. Please enter only an employee position from the list"


def calculate_net_monthly_employee_income(hourly_rate, employee_monthly_hours):
    gross_income = employee_monthly_hours * hourly_rate
    tax_deducted = gross_income * FIXED_INCOME_TAX / 100
    net_monthly_employee_income = gross_income - tax_deducted
    return net_monthly_employee_income


# Mock input for testing in non-interactive environments
employee_position = "chef"  # Mock input for testing
employee_monthly_hours = 160  # Mock input for testing

# Testing the script logic
output = validate_employee_position_and_calculate(employee_position, employee_monthly_hours)

 



