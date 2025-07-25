import os
import unittest
from challenges.python.etl import process_csv

class TestETL(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_prices.csv"
        self.schema_file = "test_mysqlCreateSchema.sql"
        self.values_file = "test_mysqlInsertValues.sql"

        with open(self.input_file, "w") as f:
            f.write("Date,Price,Volume\n")
            f.write("2025-07-25,100.5,2000\n")
            f.write("2025-07-26,101.0,2500\n")
            f.write("2025-07-27,102.75,3000\n")

    def tearDown(self):
        os.remove(self.input_file)
        os.remove(self.schema_file)
        os.remove(self.values_file)

    def test_process_csv(self):
        process_csv(self.input_file, self.schema_file, self.values_file)

        # Check schema file
        with open(self.schema_file, "r") as f:
            schema_content = f.read()
            self.assertIn("CREATE TABLE `nasdaq_prices`", schema_content)
            self.assertIn("`Date` varchar", schema_content)
            self.assertIn("`Price` decimal", schema_content)
            self.assertIn("`Volume` int", schema_content)

        # Check values file
        with open(self.values_file, "r") as f:
            values_content = f.read()
            self.assertIn("INSERT INTO nasdaq_prices", values_content)
            self.assertIn("2025-07-25", values_content)
            self.assertIn("100.5", values_content)
            self.assertIn("2000", values_content)


if __name__ == "__main__":
    unittest.main()