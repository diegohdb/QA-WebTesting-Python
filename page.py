import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import ast


class BasePage:
    """
    Base Page class that hold common elements
    and functionalities to all pages in app
    """
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_elem_text(self, by_locator, elem_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == elem_text

    def is_clickable(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))

    def send_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def send_file(self, id, file_path):
        self.driver.find_element_by_id(id).send_keys(os.getcwd() + file_path)

    def get_elem(self, by_locator, waitfor=20):
        return WebDriverWait(self.driver, waitfor).until(EC.visibility_of_element_located(by_locator))

    def choose(self, drop_down_sel_id, value):
        select = Select(self.driver.find_element_by_id(drop_down_sel_id))
        select.select_by_visible_text(value)

    def assert_email(self, css_locator, color):
        el = self.driver.find_element_by_css_selector(css_locator)
        rgba = el.value_of_css_property("color")
        r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        assert hex_value == color

    def clear_area(self, by_locator, waitfor=20):
        return WebDriverWait(self.driver, waitfor).until(EC.visibility_of_element_located(by_locator)).clear()


class ContactPage(BasePage):
    """
    Contact Form page
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://automationpractice.com/index.php?controller=contact")
        self.default_subject = 'Customer service'
        self.default_email = 'tester@test.com'
        self.default_order = 'Test'
        self.default_message = 'Test'
