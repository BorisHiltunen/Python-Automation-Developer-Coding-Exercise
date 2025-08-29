from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--headless")
options.page_load_strategy = "eager"


class FormReader():
    """Class that contains functions for establing a connection and using the relevant form."""

    def __init__(self, form_page, performance_mode) -> None:
        """Initialize necessary values for the FormReader"""
        self.form_page = form_page
        self.performance_mode = performance_mode
        self.driver = self.open_form_page()

    def open_form_page(self) -> None:
        """Opens the web page that was initialized earlier."""
        if self.performance_mode:
            driver = webdriver.Firefox(options=options)
        else:
            driver = webdriver.Firefox()
        driver.get(self.form_page)
        return driver

    def click_start(self) -> None:
        """Clicks the start button to start the challenge."""
        start_button = self.driver.find_element(By.XPATH, "//*[text()='Start']")
        start_button.click()

    def fill_form_fields(self, excel_data) -> None:
        """Fills the form page's fields with the previously fetched excel data."""
        if self.performance_mode:
            self.fill_forms_faster(excel_data)
        else:
            self.fill_forms_normally(excel_data)

    def fill_forms_faster(self, excel_data) -> None:
        """
        Fills forms by using zip to loop through the dataframe
        using css_selectors to find elements more efficiently.
        """
        d = excel_data
        for f, l, c, r, a, e, p in zip(d['First Name'], d['Last Name '], d['Company Name'], d['Role in Company'], d['Address'], d['Email'], d['Phone Number']):
            self.fill_fields(f, l, c, r, a, e, p)
            self.click_submit()

    def fill_fields(self, f, l, c, r, a, e, p) -> None:
        """Fills fields with the fetched data."""
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelFirstName']"
        ))).send_keys(f)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelLastName']"
        ))).send_keys(l)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelCompanyName']"
        ))).send_keys(c)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelRole']"
        ))).send_keys(r)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelAddress']"
        ))).send_keys(a)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelEmail']"
        ))).send_keys(e)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='labelPhone']"
        ))).send_keys(p)

    def fill_forms_normally(self, excel_data) -> None:
        """Fills forms by going through the excel rows and submits the data after."""
        field_names = self.get_field_names()
        for _, excel_row in excel_data.iterrows():
            for key, value in excel_row.items():
                label_name = field_names[key.strip()]
                element = self.driver.find_element(By.XPATH, f"//*[@ng-reflect-name='{label_name}']")
                element.send_keys(value)
                assert str(element.get_property("value")) == str(value)
            self.click_submit()

    def get_field_names(self) -> dict:
        """Returns a helper dict that contains columns and their field_names."""
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

    def click_submit(self) -> None:
        """Clicks the 'Submit' button."""
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Submit"]'
        ))).click()
    
    def check_result(self) -> None:
        """Prints the run's result."""
        result = self.driver.find_element(By.XPATH, "//*[contains(text(), 'milliseconds')]")
        print(result.text)

    def close_form_page(self) -> None:
        """Closes the form page."""
        self.driver.quit()
