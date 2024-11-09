import unittest
from devops_a2 import calculate_net_monthly_employee_income

class TestEmployeeIncomeCalculation(unittest.TestCase):
    
    # Successful Test Cases
    def test_chef_income(self):
        # Test for a chef working 160 hours in a month
        hourly_rate = 30  # CHEF_HOURLY_RATE
        hours_worked = 160
        expected_income = 160 * hourly_rate * (1 - 0.18)
        self.assertAlmostEqual(calculate_net_monthly_employee_income(hourly_rate, hours_worked), expected_income)
    
    def test_waiter_income(self):
        # Test for a waiter working 140 hours in a month
        hourly_rate = 28  # WAITER_HOURLY_RATE
        hours_worked = 140
        expected_income = 140 * hourly_rate * (1 - 0.18)
        self.assertAlmostEqual(calculate_net_monthly_employee_income(hourly_rate, hours_worked), expected_income)
    
    def test_cleaner_income(self):
        # Test for a cleaner working 100 hours in a month
        hourly_rate = 24  # CLEANER_HOURLY_RATE
        hours_worked = 100
        expected_income = 100 * hourly_rate * (1 - 0.18)
        self.assertAlmostEqual(calculate_net_monthly_employee_income(hourly_rate, hours_worked), expected_income)
    
    # Failing Test Cases
    def test_incorrect_income_calculation(self):
        # Incorrect expected value to force a failure
        hourly_rate = 30  # CHEF_HOURLY_RATE
        hours_worked = 160
        incorrect_expected_income = 160 * hourly_rate  # Ignoring tax deduction
        self.assertNotEqual(calculate_net_monthly_employee_income(hourly_rate, hours_worked), incorrect_expected_income)
    
    def test_negative_hours(self):
        # Test with negative hours worked
        hourly_rate = 25  # DELIVERY_HOURLY_RATE
        hours_worked = -10  # Invalid case
        self.assertLess(calculate_net_monthly_employee_income(hourly_rate, hours_worked), 0)

if __name__ == '__main__':
    unittest.main()
