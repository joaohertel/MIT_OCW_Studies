import unittest
import ps1_problem_1

class TestMain(unittest.TestCase):

  def test_f(self):

    # inputs for the test
    outstanding_balance = 4800
    annual_interest_rate = .2
    minimum_monthly_payment_rate = .02
    
    # expected answer
    answer = {
      'num_months':1
    }

    # number_months_to_pay
    num = 10
    result = ps1_problem_1.main()

    self.assertEqual(result, 4)


unittest.main()