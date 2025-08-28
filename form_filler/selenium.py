from selenium import webdriver
from selenium.webdriver.common.by import By


class FormReader():
    """Class that contains functions for establing a connection and using the relevant form."""

    def __init__(self, form_page) -> None:
        """Initialize necessary values for the FormReader"""
        self.form_page = form_page
        self.driver = self.open_form_page()

    def open_form_page(self) -> None:
        """Opens the web page that was initialized earlier."""
        driver = webdriver.Firefox()
        driver.get(self.form_page)
        return driver

    def click_start(self) -> None:
        """Clicks the start button to start the challenge."""
        start_button = self.driver.find_element(By.XPATH, "//*[text()='Start']")
        start_button.click()

    def fill_form_fields(self, excel_data, field_names, performance_mode) -> None:
        """Fills the form page's fields with the previously fetched excel data."""
        if performance_mode:
            self.fill_forms_fast(excel_data, field_names)
        else:
            self.fill_forms_normally(excel_data, field_names)

    def fill_forms_fast(self, excel_data, field_names) -> None:
        """Fills forms by using itertuples thus making the loop process more efficient."""
        for excel_row in excel_data.itertuples():
            for index in range(1, 8):
                label_name = field_names[str(index)]
                element = self.driver.find_element(By.XPATH, fr"//*[@ng-reflect-name='{label_name}']")
                element.send_keys(excel_row[index])
                assert str(element.get_property("value")) == str(excel_row[index])
            self.click_submit()

    def fill_forms_normally(self, excel_data, field_names) -> None:
        """Fills forms by going through the excel rows and submits the data after."""
        for _, excel_row in excel_data.iterrows():
            for key, value in excel_row.items():
                label_name = field_names[key.strip()]
                element = self.driver.find_element(By.XPATH, fr"//*[@ng-reflect-name='{label_name}']")
                element.send_keys(value)
                assert str(element.get_property("value")) == str(value)
            self.click_submit()

    def click_submit(self) -> None:
        """Clicks the 'Submit' button."""
        submit_element = self.driver.find_element(By.XPATH, "//*[@value='Submit']")
        submit_element.click()
    
    def close_form_page(self) -> None:
        """Closes the form page."""
        self.driver.quit()
