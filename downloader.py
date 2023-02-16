import pandas as pd
from seleniumwire import webdriver
from selenium import webdriver as sel
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email import header
from collections import ChainMap
from collections import deque
from tqdm import tqdm
import json
import requests as r
import time
import os


class SeleniumHelper():
    '''
    @author : Sourav Choudhury
    @Params : None

    @Job    : Contains functions to automate process on the WEB APP
    '''

    def __init__(self) -> None:
        pass

    @classmethod
    def getChromeDriver(cls, download_folder="downloads", headless=False):
        '''
        @author : Sourav Choudhury
        @Params : download_folder - Download folder location in the current directory
                  headless        - Option to make ChromeDriver headless

        @Job    : Returns a ChromeDriver instance, with some default options set.
        '''
        options = webdriver.ChromeOptions()
        print("...Downloads location "+f"{os.getcwd()}\\{download_folder}")
        options.add_experimental_option('prefs', {
            # Change default directory for downloads
            "download.default_directory": f"{os.getcwd()}\\{download_folder}",
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            # It will not show PDF directly in chrome
            "plugins.always_open_pdf_externally": True
        })
        if headless:
            options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        return driver

    @classmethod
    def getWebElementByXpath(cls, driver, xpath):
        '''
        @author : Sourav Choudhury
        @Params : driver - ChromeDriver instance
                  xpath  - Xpath of the web element

        @Job    : Returns an element using xpath
        '''
        # driver = cls.getChromeDriver()
        web_element = driver.find_element(By.XPATH, xpath)
        return web_element


if __name__ == '__main__':

    BASE_URL = r"https://posoco.in/transmission-pricing/notification-of-transmission-charges-for-the-dics/"

    driver_instance = SeleniumHelper.getChromeDriver()
    driver_instance.get(BASE_URL)

    '''
    Getting the first row and downloading the PDF

    Downloading the PDF based on the date provided.

    We will send the date if it is mentioned by the user, else the script will download the latest PDF that
    is found on the portal.
    '''
    date_search_xpath = "//*[@id='wpdmmydls-9410998d21d59179198cc0f6ce3b8a42_filter']/label/input"
    search_box_element = SeleniumHelper.getWebElementByXpath(
        driver_instance, date_search_xpath)
    search_box_element.send_keys("HEllo world")

    first_record_xpath = "//*[@id='wpdmmydls-9410998d21d59179198cc0f6ce3b8a42']/tbody/tr[1]/td/a"
    first_record_element = SeleniumHelper.getWebElementByXpath(
        driver_instance, first_record_xpath)
    first_record_element.click()
    # get_download_button = "//*[@id='icon']"
    # download_button = SeleniumHelper.getWebElementByXpath(
    #     driver_instance, get_download_button)

    pass
