from form_filler import excel


def test_get_data():
    """Test for checking if the data can be fetched without problems."""
    # Fetch data from excel
    excel_path = r"files/challenge.xlsx"
    excel_reader = excel.ExcelReader(excel_path)
    excel_data = excel_reader.get_data()

    # Check that the challenge file isn't empty and it contains enough rows for the challenge
    assert len(excel_data) > 0 and len(excel_data) < 11

    # Check that the excel data contains the right columns
    columns = [
        "First Name",
        "Last Name ",
        "Company Name",
        "Role in Company",
        "Address",
        "Email",
        "Phone Number",
    ]
    assert excel_data.columns.tolist() == columns
