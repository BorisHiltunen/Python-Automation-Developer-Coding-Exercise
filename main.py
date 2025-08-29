from form_filler import excel, selenium
import argparse
from time import sleep


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
    excel_reader = excel.ExcelReader(excel_path, performance_mode)
    excel_data = excel_reader.get_data()

    # Establish a connection to the form page and open it
    form_page = "https://rpachallenge.com/"
    form_reader = selenium.FormReader(form_page, performance_mode)
    sleep(1)

    # Start the challenge
    form_reader.click_start()

    # Loop through the excel's rows by filling the form's input fields and submitting it
    form_reader.fill_form_fields(excel_data)

    # Check how the run went
    form_reader.check_result()

    # Close the page after the process is done
    form_reader.close_form_page()

if __name__ == "__main__":
    main()
