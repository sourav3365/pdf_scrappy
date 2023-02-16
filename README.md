# pdf_scrappy

### A simple automation using Selenium to extract Data from pdf files

@Job    : Executes the process to extract table from the PDF file
1. The process starts with navigating to the WEBSITE based on the value of BASE_URL
2. Using selenium the PDF file is downloaded, using the DATE as filter
3. The downloaded file is then parsed through PDFreader and tabula to get the required DataFrames
   The dataframes are extracted based on the TABLE_NAME provided
4. The Dataframes are concated and some transformation is performed
5. The Dataframe is saved as an excel file in the Current directory


How to execute program.
1. Download the zip file
2. Install required libraries
3. Execute the runner.py program
4. If there is an issues encountered with Chromdriver. Visit here -> https://chromedriver.chromium.org/downloads, download the required driver, keep it in the same    directory and then execute the runner.py script
