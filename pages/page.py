import os
import shutil
import time
from pathlib import Path

import keyboard
import pyautogui
from selenium.common import WebDriverException, NoSuchElementException

from data.locators import TestPageLocators
from pages.base_page import BasePage
from tests.base_test import config


class Page(BasePage):
    shutil.rmtree(Path(__file__).parent / "../results")
    os.mkdir(Path(__file__).parent / "../results")

    def __init__(self, driver, wait):
        self.locator = TestPageLocators
        super().__init__(driver, wait)

    def go_to_test_page(self):
        try:
            self.go_to_page(config()['url'])
        except WebDriverException:
            raise WebDriverException('Incorrect url entered')

    def login(self):
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()

        time.sleep(5)
        pyautogui.typewrite(config()['login'])
        keyboard.press('enter')

        time.sleep(2)
        pyautogui.typewrite(config()['password'])
        keyboard.press('enter')

        time.sleep(5)
        if 'Войти в электронную почту Mail.ru' in self.get_title():
            self.driver.save_screenshot("results/results_login.png")
            raise AssertionError('Incorrect login or password entered')

    def send_message(self):
        self.driver.find_element(*self.locator.SEND_MESSAGE_BUTTON).click()

        time.sleep(5)
        self.driver.find_element(*self.locator.ADDRESS_INPUT).send_keys(config()['address_list'])
        self.driver.find_element(*self.locator.SUBJECT_INPUT).send_keys(config()['subject'])
        self.driver.find_element(*self.locator.TEXT_INPUT).send_keys(config()['text'])
        self.driver.find_element(*self.locator.SEND_BUTTON).click()

        try:
            time.sleep(5)
            self.driver.find_element(*self.locator.INCORRECT_ADDRESS_MESSAGE)
        except NoSuchElementException:
            pass
        else:
            self.driver.save_screenshot("results/results_send_message.png")
            raise AssertionError('Incorrect mail address entered')
