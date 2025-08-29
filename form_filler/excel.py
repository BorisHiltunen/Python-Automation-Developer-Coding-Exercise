import pandas as pd


class ExcelReader():
    """Class that contains functions for reading the relevant excel."""

    def __init__(self, excel_path, performance_mode) -> None:
        """Initialize necessary values for the ExcelReader"""
        self.excel_path = excel_path
        self.performance_mode = performance_mode

    def get_data(self) -> dict:
        """Returns the excel data as a dataframe."""
        df = pd.read_excel(self.excel_path)
        return df
