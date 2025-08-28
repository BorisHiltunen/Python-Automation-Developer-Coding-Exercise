import pandas as pd


class ExcelReader():
    """Class that contains functions for reading the relevant excel."""

    def __init__(self, excel_path) -> None:
        """Initialize necessary values for the ExcelReader"""
        self.excel_path = excel_path

    # TODO Needs to be checked if the data needs to be formatted here
    def get_data(self) -> dict:
        """Returns the excel data as a dataframe."""
        df = pd.read_excel(self.excel_path)
        return df
