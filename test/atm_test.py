import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from atm import ATM, InvalidPinException, InsufficientFundsException


class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()
        self.correct_pin = 1234
        self.wrong_pin = 0000

    # Testy check_balance
    def test_check_balance_correct_pin(self):
        self.atm._balance = 100.0
        self.assertEqual(self.atm.check_balance(self.correct_pin), 100.0)

    def test_check_balance_wrong_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(self.wrong_pin)

    # Testy deposit
    def test_deposit_correct_pin(self):
        self.assertEqual(self.atm.deposit(self.correct_pin, 50.0), 50.0)

    def test_deposit_wrong_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(self.wrong_pin, 50.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(self.correct_pin, -10.0)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(self.correct_pin, 0.0)

    # Testy withdraw
    def test_withdraw_correct_pin_sufficient_funds(self):
        self.atm._balance = 100.0
        self.assertEqual(self.atm.withdraw(self.correct_pin, 50.0), 50.0)

    def test_withdraw_correct_pin_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(self.correct_pin, 50.0)

    def test_withdraw_wrong_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(self.wrong_pin, 50.0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(self.correct_pin, -50.0)

    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(self.correct_pin, 0.0)

if __name__ == '__main__':
    unittest.main()
