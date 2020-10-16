import unittest
from selenium import webdriver
from page import ContactPage
from locators import ContactPageLocators


class TestContactBase(unittest.TestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('headless')
        self.driver = webdriver.Firefox(options=firefox_options)

    def tearDown(self):
        self.driver.quit()


class TestContact(TestContactBase):

    def setUp(self):
        super().setUp()
        self.contact = ContactPage(self.driver)

    def test_send_message_with_empty_text(self):
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG, 'Invalid email address.')

    def test_send_message_no_subject_selected(self):
        self.contact.send_text(ContactPageLocators.EMAIL, self.contact.default_email)
        self.contact.send_text(ContactPageLocators.ORDER, self.contact.default_order)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG, 'Please select a subject from the list provided.')

    def test_send_message_no_email(self):
        self.contact.choose(ContactPageLocators.SUBJECT_SELECTION, self.contact.default_subject)
        self.contact.send_text(ContactPageLocators.ORDER, self.contact.default_order)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG, 'Invalid email address.')

    def test_send_message_no_order(self):
        self.contact.choose(ContactPageLocators.SUBJECT_SELECTION, self.contact.default_subject)
        self.contact.send_text(ContactPageLocators.EMAIL, self.contact.default_email)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG_SEND,
                                      'Your message has been successfully sent to our team.')

    def test_email_validation(self):
        invalid_email = ['Abc.example.com', 'A@b@c@example.com', '****asd@example.com',
                         'just""""not""""right@example.com', 'this is""""not\\allowed@example.com',
                         'this\\ still\\""""not\\allowed@example.com',
                         '1234567890123456789012345678901234567890123456789012345678901234+x@example.com',
                         'john..doe@example.com', 'example@localhost', 'john.doe@example..com',
                         '\"\"\"\"test.more test \"\"\"\"@example.com']

        for email in invalid_email:
            with self.subTest(email):
                self.contact.clear_area(ContactPageLocators.EMAIL)
                self.contact.send_text(ContactPageLocators.EMAIL, email)
                self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
                # This is assert for an invalid email based on the validation color
                self.contact.assert_email(ContactPageLocators.EMAIL_COLOR, '#f13340')
        self.contact.send_text(ContactPageLocators.EMAIL, self.contact.default_email)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        # Assert for valid email
        self.contact.assert_email(ContactPageLocators.EMAIL_COLOR, '#35b33f')

    def test_attachment_less_than_limit(self):
        self.contact.choose(ContactPageLocators.SUBJECT_SELECTION, self.contact.default_subject)
        self.contact.send_text(ContactPageLocators.EMAIL, self.contact.default_email)
        self.contact.send_text(ContactPageLocators.ORDER, self.contact.default_order)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        self.contact.send_file(ContactPageLocators.FILE_UPLOAD, '/test_data/less_than_2mb.png')
        self.contact.assert_elem_text(ContactPageLocators.FILE_NAME, 'less_than_2mb.png')
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG_SEND, 'Your message has been successfully sent to our team.')

    def test_attachment_greater_than_limit(self):
        self.contact.choose(ContactPageLocators.SUBJECT_SELECTION, self.contact.default_subject)
        self.contact.send_text(ContactPageLocators.EMAIL, self.contact.default_email)
        self.contact.send_text(ContactPageLocators.ORDER, self.contact.default_order)
        self.contact.send_text(ContactPageLocators.MESSAGE, self.contact.default_message)
        self.contact.send_file(ContactPageLocators.FILE_UPLOAD, '/test_data/greater_than_2mb.mp4')
        self.contact.assert_elem_text(ContactPageLocators.FILE_NAME, 'greater_than_2mb.mp4')
        self.contact.click(ContactPageLocators.SEND_BUTTON)
        assert not self.contact.assert_elem_text(ContactPageLocators.ALERT_MSG_SEND, 'Your message has been successfully sent to our team.')


if __name__ == '__main__':
    unittest.main()
