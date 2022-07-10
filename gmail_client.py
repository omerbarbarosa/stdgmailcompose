import time
from typing import KeysView
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GmailClient:

    def __init__(self):
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.driver = uc.Chrome(use_subprocess=True)
        self.time = 600

    def login(self, email, password):
        self.driver.get("https://mail.google.com/")
        user_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'identifierId')))

        user_input.send_keys(f'{email}\n')
        user_input.send_keys(Keys.RETURN)
         time.sleep(10)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(
            f'{password}\n')

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(
            Keys.RETURN)

    def send_email(self, to, subject, body):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//*[contains(@class, 'T-I T-I-KE L3')]").click()
        time.sleep(2)
        to_input = self.driver.find_element(By.XPATH, '//*[@name="to"]')
        to_input.send_keys(to)
        to_input.send_keys(Keys.RETURN)
        subject_input = self.driver.find_element(By.XPATH, '//*[@name="subjectbox"]')
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.RETURN)
        body_input = self.driver.find_element(By.XPATH, '//*[@class="Am Al editable LW-avf tS-tW"]')
        body_input.send_keys(body)
        self.driver.find_element(By.XPATH, '//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3 T-I-KL"]').click()

    def mail_list(self):
        time.sleep(15)
        table_rows = self.driver.find_elements(By.XPATH, '//table[@class="F cf zt"]//tr')
        all_emails = []

        # for row in table_rows:
        #     all_emails.append(row.find_element(By.XPATH, './/td//span[3]').text())

        return all_emails

    def stared(self, text):
        time.sleep(20)
        table_rows = self.driver.find_elements(By.XPATH, '//table[@class="F cf zt"]//tr')
        for row in table_rows:

            if text in row.get_attribute('innerHTML'):
                row.find_element(By.XPATH, './/td/span[@role="button"]').click()

    def delete_mail(self, text):
        time.sleep(10)
        table_rows = self.driver.find_elements(By.XPATH, '//table[@class="F cf zt"]//tr')
        a = ActionChains(self.driver)
        for row in table_rows:

            if text in row.get_attribute('innerHTML'):
                a.move_to_element(row).perform()
                row.find_element(By.XPATH, './/ul[@role="toolbar"]/li[2]').click()


if __name__ == "__main__":
    email = 'testforhomeworkis@gmail.com'  # replace email
    password = 'ZXCdsa123'  # replace password
    gmail_client = GmailClient()
    gmail_client.login(email, password)
    # gmail_client.send_email("testforhomeworkis@gmail.com", "Test mail Subject", "Test email Body")
    # gmail_client.stared("Test mail Subject")
    # gmail_client.delete_mail("Test mail Subject")
