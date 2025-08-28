import pandas as pd


class ExcelReader():

    def __init__(self, excel_path) -> None:
        self.excel_path = excel_path

    # TODO Needs to be checked if the data needs to be formatted here
    def get_data(self) -> dict:
        df = pd.read_excel(self.excel_path)
        # breakpoint()
        return df
