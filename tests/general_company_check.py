from src.data_checks.check import Check
from src.data_checks.rule import rule
from hamcrest import assert_that, equal_to
import pandas as pd
import os


class GeneralCompanyTransactionCheck(Check):
    def __init__(self):
        super().__init__()
        self.category = "Consistency"
        self.rules_params = {
            "company_payments_size_increasing": [
                {"args": (), "kwargs": {"company_name": "company_name"}}
            ],
        }

    @rule(
        name="Company Payments Size Increasing",
        description="Size of the payments dataframe is increasing",
    )
    def company_payments_size_increasing(self, company_name, days=[2, 5]):
        old_payments_df = pd.read_csv(
            os.path.dirname(os.path.realpath(__file__)) + "/old_payments.csv"
        )
        new_payments_df = pd.read_csv(
            os.path.dirname(os.path.realpath(__file__)) + "/new_payments.csv"
        )
        assert_that(
            new_payments_df.shape[0] >= old_payments_df.shape[0],
            equal_to(True),
            f"Size of the payments dataframe has decreased in the last few days",
        )
