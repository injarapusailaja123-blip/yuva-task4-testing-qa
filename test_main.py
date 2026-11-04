import unittest
import os
from src.main import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_expenses.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.tracker = ExpenseTracker(filename=self.test_file)
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    def test_add_expense(self):
        result = self.tracker.add_expense("Food", 200)
        self.assertTrue(result)
        self.assertEqual(self.tracker.calculate_total(), 200)
    def test_add_multiple(self):
        self.tracker.add_expense("Food", 200)
        self.tracker.add_expense("Bus", 50)
        self.assertEqual(self.tracker.calculate_total(), 250)
    def test_view_empty(self):
        self.assertEqual(self.tracker.view_expenses(), [])
    def test_delete_expense(self):
        self.tracker.add_expense("Food", 200)
        result = self.tracker.delete_expense("Food")
        self.assertTrue(result)
        self.assertEqual(len(self.tracker.expenses), 0)
    def test_delete_non_existing(self):
        self.assertFalse(self.tracker.delete_expense("Pizza"))
    def test_calculate_total(self):
        self.tracker.add_expense("Food", 200)
        self.tracker.add_expense("Bus", 50)
        self.assertEqual(self.tracker.calculate_total(), 250)
    def test_empty_input(self):
        self.assertFalse(self.tracker.add_expense("", 0))
    def test_invalid_amount(self):
        self.assertFalse(self.tracker.add_expense("Food", "abc"))
    def test_negative_amount(self):
        self.assertFalse(self.tracker.add_expense("Food", -100))
    def test_file_save_load(self):
        self.tracker.add_expense("Food", 200)
        new_tracker = ExpenseTracker(filename=self.test_file)
        self.assertEqual(len(new_tracker.expenses), 1)
        self.assertEqual(new_tracker.calculate_total(), 200)

if __name__ == "__main__":
    unittest.main()