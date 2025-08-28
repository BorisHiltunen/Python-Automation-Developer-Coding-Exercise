from form_filler import excel, selenium


def main() -> None:
    # Fetch data from excel
    excel_path = r"files/challenge.xlsx"
    excel_reader = excel.ExcelReader(excel_path)
    excel_data = excel_reader.get_data()

    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page)
    # form_reader.click_start()

    # Loop through the excel's rows by filling the form's input fields and submitting it
    for _, excel_row in excel_data.iterrows():
        form_reader.fill_form_fields(excel_row)

    # Close the page after the process is done
    form_reader.close_form_page()

if __name__ == "__main__":
    main()
