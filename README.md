# pdf_scrappy

### A simple automation using Selenium to extract Data from pdf files

@Job    : Executes the process to extract table from the PDF file
1. The process starts with navigating to the WEBSITE based on the value of BASE_URL
2. Using selenium the PDF file is downloaded, using the DATE as filter
3. The downloaded file is then parsed through PDFreader and tabula to get the required DataFrames
   The dataframes are extracted based on the TABLE_NAME provided
4. The Dataframes are concated and some transformation is performed
5. The Dataframe is saved as an excel file in the Current directory
