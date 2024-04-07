from selenium.webdriver.common.by import By


class TestPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//*[@id='mailbox']/div[1]/button")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//*[@id='app-canvas']/div/div[1]/div[1]/div/div[2]/span/div[1]/div["
                                     "1]/div/div/div/div[1]/div/div/a")
    ADDRESS_INPUT = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div/div/div[1]/div/div["
                               "2]/div/div/label/div/div/input")
    SUBJECT_INPUT = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/input")
    TEXT_INPUT = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/div[4]/div/div/div[2]/div[1]/div[2]")
    SEND_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div/button")
    INCORRECT_ADDRESS_MESSAGE = (By.XPATH, "/html/body/div[19]")
