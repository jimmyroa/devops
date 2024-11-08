import unittest

# Import the original code functions
from devops_a2 import validate_employee_position_and_calculate, calculate_net_monthly_employee_income

class TestEmployeeSalary(unittest.TestCase):
    def test_chef_calculation_success(self):
        """Test case 1: Test successful calculation of chef's net salary (should pass)"""
        # Capture the printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Test execution
        validate_employee_position_and_calculate('chef', 160)
        sys.stdout = sys.__stdout__  # Reset redirect
        
        expected_net_income = 3936.0  # (30 * 160) * (1 - 0.18)
        expected_output = "CHEF\nNet monthly income:3936.0"
        self.assertIn(expected_output, captured_output.getvalue().strip())

    def test_waiter_direct_calculation_success(self):
        """Test case 2: Test direct calculation of waiter's net income (should pass)"""
        result = calculate_net_monthly_employee_income(28, 100)  # Using WAITER_HOURLY_RATE
        expected = 2296.0  # (28 * 100) * (1 - 0.18)
        self.assertEqual(result, expected)

    def test_delivery_case_insensitive_success(self):
        """Test case 3: Test case-insensitive position input (should pass)"""
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        validate_employee_position_and_calculate('DELIVERY', 120)
        sys.stdout = sys.__stdout__

        expected_net_income = 2460.0  # (25 * 120) * (1 - 0.18)
        expected_output = "DELIVERY\nNet monthly income:2460.0"
        self.assertIn(expected_output, captured_output.getvalue().strip())

    def test_invalid_position_fail(self):
        """Test case 4: Test invalid position input (should fail)"""
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        validate_employee_position_and_calculate('manager', 100)
        sys.stdout = sys.__stdout__

        expected_output = "Invalid input. please enter only an employee position from the list"
        self.assertIn(expected_output, captured_output.getvalue().strip())

    def test_missing_parameter_fail(self):
        """Test case 5: Test with missing required parameter (should fail)"""
        with self.assertRaises(TypeError):
            validate_employee_position_and_calculate('cleaner')  # Missing monthly_hours parameter

if __name__ == '__main__':
    unittest.main()