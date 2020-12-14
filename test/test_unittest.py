import unittest
from unittest import result
import pandas as pd
from nose.tools import assert_true
import requests

from app import clean_final_dataset, create_final_dataset, query_example


class test_clean_final_dataset(unittest.TestCase):
    def ftesting_cleaning_dataset(self):
        """
        test cleaning final dataset
        """
        d_ugly = {"x12": ["($12,000)"], "x62": ["67%"]}
        d_clean = {"x12": [12000.0], "x62": [67.0]}
        df_cleaned = pd.DataFrame(data=d_clean)
        df = pd.DataFrame(data=d_ugly)
        df_not_ugly = clean_final_dataset(df)
        result = df_not_ugly.equals(df_cleaned)
        self.assertTrue(result)


class test_create_final_dataset(unittest.TestCase):
    def testing_create_dataset(self):
        """
        test cleaning final dataset
        """
        df_test = pd.read_csv("./test/create_test_db.csv")
        df_right_answer = pd.read_csv("./test/df_final_test.csv")
        df_test_final = clean_final_dataset(df_test)
        result = df_test_final.equals(df_right_answer)
        self.assertTrue(result)


class test_query_example(unittest.TestCase):
    def test_request_response(self):
        """
        run main function
        """

        # Send a request to the API server and store the response.
        response = requests.get("http://jsonplaceholder.typicode.com/todos")

        # Confirm that the request-response cycle completed successfully.
        self.assert_true(response.ok)


if __name__ == "__main__":
    unittest.main()
