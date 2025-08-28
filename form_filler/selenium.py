from selenium import webdriver
from selenium.webdriver.common.by import By


class FormReader():

    def __init__(self, form_page) -> None:
        self.form_page = form_page
        self.driver = self.open_form_page()

    def open_form_page(self) -> None:
        driver = webdriver.Firefox()
        driver.get(self.form_page)
        return driver
    
    def add_excel_data(self, excel_data) -> None:
        self.fill_name_fields(excel_data)

    def fill_name_fields(self, excel_data) -> None:
        first_name_element = self.driver.find_element(By.XPATH, fr"//*[@ng-reflect-name='labelFirstName']")
        first_name_element.send_keys("test")
    
        last_name_element = self.driver.find_element(By.XPATH, fr"//*[@ng-reflect-name='labelLastName']")
        last_name_element.send_keys("test")
        # breakpoint()
