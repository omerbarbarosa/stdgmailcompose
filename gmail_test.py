import time
import unittest
from gmail_client import GmailClient

INBOX = "https://mail.google.com/mail/u/0/#inbox"


class TestGmail(unittest.TestCase):
    def setUp(self):
        self.gmail_client = GmailClient()

    def __login(self,email,password):
        self.gmail_client.login(email, password)
        time.sleep(10)

    def test_login(self):
        self.__login('testforhomeworkis@gmail.com','ZXCdsa123')
        self.assertEqual(INBOX, self.gmail_client.driver.current_url)

    def test_negative_login(self):
        self.__login('testforhomeworkis@gmail.com', 'ZXCdsa1235')
        self.assertNotEqual(INBOX, self.gmail_client.driver.current_url)

    def test_send_email(self):
        self.gmail_client.send_email("testforhomeworkis@gmail.com", "Test mail Subject", "Test email Body")

if __name__ == "__main__":
    unittest.main()
