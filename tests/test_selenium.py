import pandas as pd
from form_filler import selenium
from time import sleep


def test_open_form_page() -> None:
    """Test for checking if the form page can be opened without problems."""
    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page)
    sleep(1)
    # Close the form page after it was opened succesfully
    form_reader.close_form_page()


def test_form_fields() -> None:
    """Test for checking if the form page's input fields can be edited succesfully."""
    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page)

    test_data = {
        "First Name": ["testFirstName"],
        "Last Name ": ["testLastName"],
        "Company Name": ["testCompanyName"],
        "Role in Company": ["testRole"],
        "Address": ["testAddress"],
        "Email": ["testEmail"],
        "Phone Number": ["testPhone"],
    }
    # Create DataFrame
    excel_data = pd.DataFrame(test_data)
    for _, excel_row in excel_data.iterrows():
        form_reader.fill_form_fields(excel_row)

    sleep(2)
    # Close the form page after it was opened succesfully
    form_reader.close_form_page()
