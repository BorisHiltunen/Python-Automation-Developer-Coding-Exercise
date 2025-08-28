from form_filler import excel, selenium
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('performance_mode')
args = parser.parse_args()


def main() -> None:
    if args.performance_mode == "performance_mode":
        performance_mode = True
    else:
        performance_mode = False

    # Fetch data from excel
    excel_path = r"files/challenge.xlsx"
    excel_reader = excel.ExcelReader(excel_path)
    excel_data = excel_reader.get_data()
    field_names = excel_reader.get_field_names(performance_mode)

    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page)
    form_reader.click_start()

    # Loop through the excel's rows by filling the form's input fields and submitting it
    form_reader.fill_form_fields(excel_data, field_names, performance_mode)

    #breakpoint()
    # Close the page after the process is done
    form_reader.close_form_page()

if __name__ == "__main__":
    main()
