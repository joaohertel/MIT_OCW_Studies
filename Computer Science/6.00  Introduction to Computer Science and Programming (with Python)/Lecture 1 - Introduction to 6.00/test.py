import unittest
import ps1_problem_1
from test_data import test_results_1
# test data extracted with ChatGPT


class TestMain(unittest.TestCase):

    def test_f(self):
        
        # inputs for the test
        outstanding_balance = test_results_1["outstanding_balance"]
        annual_interest_rate = test_results_1["annual_interest_rate"]
        minimum_monthly_payment_rate = test_results_1["minimum_monthly_payment_rate"]

        result = ps1_problem_1.calculate_balance(
            outstanding_balance, annual_interest_rate, minimum_monthly_payment_rate)


        for month_number in range(1, result['num_of_months'] + 1):
            
            current_data = result['month_calculations'][month_number-1]
            test_data = test_results_1['month_calculations'][month_number-1]

            self.assertEqual(current_data["month_number"], test_data["month_number"])
            self.assertEqual(current_data["minimum_payment"], test_data["minimum_payment"])
            self.assertEqual(current_data["principle_paid"], test_data["principle_paid"])
            self.assertEqual(current_data["remaining_balance"], test_data["remaining_balance"])
        
        


unittest.main()
