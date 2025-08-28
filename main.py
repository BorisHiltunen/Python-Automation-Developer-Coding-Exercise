from form_filler import excel, selenium


def main() -> None:
    # Fetch data from excel
    excel_path = r"files/challenge.xlsx"
    excel_reader = excel.ExcelReader(excel_path)
    # excel_data = excel_reader.get_data()
    breakpoint()

    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page)
    # form_reader.open_form_page()
    # breakpoint()

if __name__ == "__main__":
    main()