import unittest

from sales_report import calculate_average, parse_sales_row


class TestSalesReport(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([100, 200, 300]), 200)

    def test_parse_sales_row(self):
        self.assertEqual(parse_sales_row("2024-01-15,Widget A,1500.00"), 1500.0)

    # Test that calculate_average raises ValueError for an empty list

    # Test that parse_sales_row raises ValueError for an amount that isn't a number


if __name__ == "__main__":
    unittest.main()
