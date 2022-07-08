import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WhatsappBot:

    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient
        self.driver = webdriver.Chrome(os.environ.get("DRIVER_PATH"))

    def open_wpp(self):
        self.driver.get('https://web.whatsapp.com')
        while True:
            try:
                self.driver.find_element_by_xpath(f"//span[@title='{self.recipient}']").click()
                break
            except Exception:
                sleep(0.25)

    def send_message(self):
        try:
            chat_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            chat_box.click()
            chat_box.send_keys(self.message + Keys.ENTER)
            sleep(1 / 100)
        except Exception:
            pass
