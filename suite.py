import unittest
from testAllFirefox import TestContact


def suite():
    suite = unittest.TestSuite()
    # Contact form page tests
    suite.addTest(TestContact('test_send_message_with_empty_text'))
    suite.addTest(TestContact('test_send_message_no_subject_selected'))
    suite.addTest(TestContact('test_send_message_no_email'))
    suite.addTest(TestContact('test_send_message_no_order'))
    suite.addTest(TestContact('test_email_validation'))
    suite.addTest(TestContact('test_attachment_less_than_limit'))
    suite.addTest(TestContact('test_attachment_greater_than_limit'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
