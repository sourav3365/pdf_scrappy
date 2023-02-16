import os
import sys
import time
from downloader import SeleniumHelper
from pdf_data_extractor import tables_finder, final_dataframe_maker
from Utils import folderHandler

BASE_URL = r"https://posoco.in/transmission-pricing/notification-of-transmission-charges-for-the-dics/"
DATE = "25-01-2023"
TABLE_NAME = "Transmission Charges for Designated ISTS Customers (DICs) for the billing month of"


def main(BASE_URL, DATE, TABLE_NAME):
    '''
    @author : Sourav Choudhury
    @Params : None

    @Job    : Executes the process to extract table from the PDF file
              1. The process starts with navigating to the WEBSITE based on the value of BASE_URL
              2. Using selenium the PDF file is downloaded, using the DATE as filter
              3. The downloaded file is then parsed through PDFreader and tabula to get the required DataFrames
                 The dataframes are extracted based on the TABLE_NAME provided
              4. The Dataframes are concated and some transformation is performed
              5. The Dataframe is saved as an excel file in the Current directory
    '''
    try:
        print('-----------------------')
        print('Starting Process')
        print('-----------------------')
        folderHandler.create_folder("downloads")

        driver_instance = SeleniumHelper.getChromeDriver()
        driver_instance.get(BASE_URL)

        date_search_xpath = "//*[@id='wpdmmydls-9410998d21d59179198cc0f6ce3b8a42_filter']/label/input"
        search_box_element = SeleniumHelper.getWebElementByXpath(
            driver_instance, date_search_xpath)
        search_box_element.send_keys(DATE)

        first_record_xpath = "//*[@id='wpdmmydls-9410998d21d59179198cc0f6ce3b8a42']/tbody/tr[1]/td/a"
        first_record_element = SeleniumHelper.getWebElementByXpath(
            driver_instance, first_record_xpath)
        first_record_element.click()
        time.sleep(5)
        print("...Download of folder completed - Date filter used {}".format(DATE))
        print("...Extracting data from PDF")
        pdf_path = folderHandler.get_file_from_folder("downloads")
        total_table_found = tables_finder(pdf_path, TABLE_NAME)
        final_dataframe_maker(total_table_found, "NEW.xlsx")

    except Exception as e:
        sys.exit(f"...{str(e)}")


if __name__ == "__main__":
    main(BASE_URL, DATE, TABLE_NAME)
