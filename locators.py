from selenium.webdriver.common.by import By


class CommonPageLocators:
    pass


class ContactPageLocators:
    SUBJECT_SELECTION = 'id_contact'
    EMAIL = (By.ID, 'email')
    EMAIL_COLOR = 'input#email.form-control.grey.validate'
    ORDER = (By.ID, 'id_order')
    FILE_UPLOAD = 'fileUpload'
    FILE = (By.CLASS_NAME, 'form-control')
    FILE_NAME = (By.CLASS_NAME, 'filename')
    MESSAGE = (By.ID, 'message')
    SEND_BUTTON = (By.ID, 'submitMessage')
    ALERT_MSG = (By.XPATH, '//*[@id="center_column"]/div/ol/li')
    ALERT_MSG_SEND = (By.XPATH,  '//*[@id="center_column"]/p')
