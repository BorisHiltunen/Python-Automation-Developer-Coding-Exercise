import pandas as pd


class ExcelReader():
    """Class that contains functions for reading the relevant excel."""

    def __init__(self, excel_path) -> None:
        """Initialize necessary values for the ExcelReader"""
        self.excel_path = excel_path

    def get_data(self) -> dict:
        """Returns the excel data as a dataframe."""
        df = pd.read_excel(self.excel_path)
        return df

    def get_field_names(self, performance_mode) -> dict:
        """Returns a helper dict that contains columns and their field_names."""
        if performance_mode:
            field_names = {
                "1": "labelFirstName",
                "2": "labelLastName",
                "3": "labelCompanyName",
                "4": "labelRole",
                "5": "labelAddress",
                "6": "labelEmail",
                "7": "labelPhone",
            }
        else:
            field_names = {
                "First Name": "labelFirstName",
                "Last Name": "labelLastName",
                "Company Name": "labelCompanyName",
                "Role in Company": "labelRole",
                "Address": "labelAddress",
                "Email": "labelEmail",
                "Phone Number": "labelPhone",
            }

        return field_names
