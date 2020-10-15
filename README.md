<h1 align="left">:computer: QA-WebTesting-Python  </h1>

Testing automation for web application using Selenium and Python

## Introduction
This project contains an automated test suite for the Contact Form page input validation from the website <a href="http://automationpractice.com/index.php?controller=contact">Automation Practice</a>. 

The test suite was built for study purpose and contains 7 functional test cases automated using Selenium and Python. 

**Note:** The test planning in a real project for this page should not be limited to test suite designed in this project.  


## Test Suite
The automated suite were designed to cover the functionality of contact form validation. The 7 test cases that were implemented will be described in the last section. 

* TC01 - Send a message with no text
* TC02 - Send a message with no subject heading selected
* TC03 - Send a message with no email address
* TC04 - Send a message with no order reference value
* TC05 - Validate the email address field for different inputs
* TC06 - Validate attachment size less than limit
* TC07 - Validate attachment size greater than limit


## Environment Setup
**Prerequisites:** 
* Python 3+ 
* pip3
* Chrome and/or Firefox webdrivers
* Update the driver in the root folder with the version of the browser on which you want to run the tests.

Check the webdrivers documentation:
- Chrome: https://chromedriver.chromium.org/getting-started
- Firefox (geckodriver): Great tutorial for Ubuntu (https://medium.com/beelabacademy/baixando-e-configurando-o-geckodriver-no-ubuntu-dc2fe14d91c)


1. Clone the project

2. Create and activate a virtualenv:
```
virtualenv --python=/usr/bin/python3.7 automation_suite 
```
```
source automation_suite/bin/activate
```

3. To install the required dependencies issue the below command in project root directory.
```
pip3 install -r requirements.txt
```

Currently supported browsers:
- Chrome
- Firefox



## How to run?

Run one test case or the whole suite using Chrome or Firefox web browser.

- Run the suite:
Issue the below commands in project root directory
```
python3 suite.py
```

- Run specific test cases: 
Issue the below commands in project root directory
```
python3 -m unittest testAll.TestContact.TEST_NAME
```
_Example: python3 -m unittest testAll.TestContact.test_send_message_with_empty_text

By default it runs in Chrome browser, you can specify which browser to use as well running from testAllFirefox.py instead testAll.py.
The webdrivers were set to run headless, if need to watch the execution, please, comment the line 11 on testAll.py or testAllFirefox.py.



## Test Cases
#### TC01 - Send a message with no text
|                             Preconditions                            |                              Steps                              |                                     Expected Results                                     |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |                              1. Customer service is loaded.                              |
|                                                                      |                    2. Click on 'Send' button.                   | 2. The message is not sent and some warning is presented asking to user fill the fields. |

#### TC02 - Send a message with no subject heading selected

|                             Preconditions                            |                              Steps                              |                                      Expected Results                                     |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |                               1. Customer service is loaded.                              |
|                                                                      |        2. Insert 'test@test.com' in Email address field.        |                          2. The email is validated and accepted.                          |
|                                                                      |            3. Insert 'Test' in Order reference field.           |                              3. The field receives the input.                             |
|                                                                      |              4. Insert 'Test' in Message box field.             |                              4. The field receives the input.                             |
|                                                                      |                    5. Click on 'Send' button                    | 5. The message is not sent and some warning is presented asking to user choose a subject. |


#### TC03 - Send a message with no email address
|                             Preconditions                            |                              Steps                              |                                      Expected Results                                     |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |                               1. Customer service is loaded.                              |
|                                                                      |              2. Select any subject heading option.              |                                  2. Selection is updated.                                 |
|                                                                      |            3. Insert 'Test' in Order reference field.           |                              3. The field receives the input.                             |
|                                                                      |              4. Insert 'Test' in Message box field.             |                              4. The field receives the input.                             |
|                                                                      |                    5. Click on 'Send' button                    | 5. The message is not sent and some warning is presented asking to a valid email address. |



#### TC04 - Send a message with no order reference value
|                             Preconditions                            |                              Steps                              |                                      Expected Results                                     |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |                               1. Customer service is loaded.                              |
|                                                                      |        2. Insert 'test@test.com' in Email address field.        |                          2. The email is validated and accepted.                          |
|                                                                      |            3. Insert 'Test' in Order reference field.           |                              3. The field receives the input.                             |
|                                                                      |              4. Insert 'Test' in Message box field.             |                              4. The field receives the input.                             |
|                                                                      |                    5. Click on 'Send' button                    | 5. The message is not sent and some warning is presented asking to user choose a subject. |


#### TC05 - Validate the email address field for different inputs

|                             Preconditions                            |                                                                                                                                                                                                                                                            Steps                                                                                                                                                                                                                                                           |             Expected Results            |
|:--------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser |                                                                                                                                                                                                                               1. On home page, click on 'Contact Us' button on the top right.                                                                                                                                                                                                                              |      1. Customer service is loaded.     |
|                                                                      | 2. Insert the following email addresses and check if it is accepted: - Abc.example.com  - A@b@c@example.com  - \*\*\*\*asd@example.com  - just""not""right@example.com  - this is""not\allowed@example.com - this\ still\""not\allowed@example.com  - 1234567890123456789012345678901234567890123456789012345678901234+x@example.com  - john..doe@example.com  - example@localhost  - john.doe@example..com  - ""test.more test ""@example.com - a valid address with a leading space - a valid address with a trailing space. |         2. No value is accepted.        |
|                                                                      |                                                                                                                                                                                                                                      3. Insert 'test@test.com' in email address field.                                                                                                                                                                                                                                     | 3. The email is validated and accepted. |


#### TC06 - Validate attachment size less than limit

|                             Preconditions                            |                              Steps                              |             Expected Results            |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:---------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |      1. Customer service is loaded.     |
|              2. Have a file with size less than 2MB size             |              2. Select any subject heading option.              |         2. Selection is updated.        |
|                                                                      |        3. Insert 'test@test.com' in email address field.        | 3. The email is validated and accepted. |
|                                                                      |            4. Insert 'Test' in Order reference field.           |     4. The field receives the input.    |
|                                                                      |              5. Insert 'Test' in Message box field.             |     5. The field receives the input.    |
|                                                                      |               6. Attach a file less than 2MB size.              |     6. The field receives the input.    |
|                                                                      |                    7. Click on 'Send' button                    |         7. The message is sent.         |


#### TC07 - Validate attachment size greater than limit

|                             Preconditions                            |                              Steps                              |                                            Expected Results                                           |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|
| 1. Access to http://automationpractice.com/index.php via web browser | 1. On home page, click on 'Contact Us' button on the top right. |                                     1. Customer service is loaded.                                    |
|            2. Have a file with size greater than 2MB size.           |              2. Select any subject heading option.              |                                        2. Selection is updated.                                       |
|                                                                      |        3. Insert 'test@test.com' in email address field.        |                                3. The email is validated and accepted.                                |
|                                                                      |            4. Insert 'Test' in Order reference field.           |                                    4. The field receives the input.                                   |
|                                                                      |              5. Insert 'Test' in Message box field.             |                                    5. The field receives the input.                                   |
|                                                                      |             6. Attach a file greater than 2MB size.             |                                    6. The field receives the input.                                   |
|                                                                      |                    7. Click on 'Send' button                    | 7. The message is not sent and some warning is presented to user warning about the size limit of 2MB. |



## Author
<a target="_blank" href="https://github.com/diegohdb/diegohdb">👤 Diego Bezerra </a>

<a target="_blank" href="https://www.linkedin.com/in/diegohdb/">
  <img align="left" alt="LinkdeIN" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a target="_blank" href="https://www.instagram.com/diegohdb/">
  <img align="left" alt="Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a target="_blank" href="mailto:diegohdb@gmail.com">
  <img align="left" alt="Gmail" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />
</a>
