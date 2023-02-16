import PyPDF2
import tabula
import sys
import os
import pandas as pd


def tables_finder(pdf_path: str, to_find: str) -> list:
    '''
    @ Last modified : 16/02/2023 (DD/MM/YYYY)


    @author : Sourav Choudhury
    @params : pdf_path - Loaction to the PDF file.
              to_find  : This is the TABLE name to search in PDF.

    @Job    : Iterate through the pages one at a time and find the required tables. The tables are found
              based on the TABLE name provided (@param : to_find). The tables will later be concated and formed into one single Dataframe
    '''
    try:
        # Read the PDF file, and get total number of pages found in the PDF
        pdfFileObj = open(pdf_path, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        total_pages_in_pdf = len(pdfReader.pages)

        # Iterate through the pages to find the required page.
        pages_found = []
        tables_found = []
        for page_number in range(total_pages_in_pdf):
            # Getting the data of the page as a String object.
            text = pdfReader.pages[page_number].extract_text().replace(
                " ", "").replace("\xa0", " ")
            if to_find in text:
                pages_found.append(page_number+1)
                dfs = tabula.read_pdf(pdf_path, pages=str(page_number+1))[0]
                tables_found.append(dfs)
                for page in range(page_number+2, total_pages_in_pdf+1):
                    continued_data = tabula.read_pdf(
                        pdf_path, pages=str(page))[0]
                    try:
                        if all(dfs.columns == continued_data.columns):
                            tables_found.append(continued_data.drop([0]))
                    except ValueError:
                        break
                break

        return tables_found

    except Exception as e:
        sys.exit(f"...{str(e)}")


def final_dataframe_maker(total_table_found: list,name="FINAL_DF.xlsx") -> pd.DataFrame:
    '''
    @ Last modified : 16/02/2023 (DD/MM/YYYY)



    @author     : Sourav Choudhury
    @params     : total_table_found - A list of dataframes

    @Why needed : It is observed that few of the column names need to adjusted, it seems to be happening because of a             merged cell of 'National Component (₹)'.
    @Job        : Make adjustment to the dataframe, concat all the dataframes in one and save as excel file.
    '''
    try:
        concatted_dataframe = pd.concat(total_table_found)
        # maps = {"National Component (₹)": "NC-RE",
        #         "Regional Component (₹)": " NC‐HVDC", "Unnamed: 0": "Total Transmission charges payable in ₹",
        #         "Transformers component (₹)": "Regional Component(₹)","Total Transmission charges payable in ₹":"Bilateral Charges (₹)"}
        '''
        We are adding a new column name at the 8th position in the list, and removing the last column name from the list
        once this is achieved, we update the column name for the concatted dataframes
        '''
        columns = list(concatted_dataframe.columns)
        columns.insert(7, "NC-HVDC")
        formatted_column_names = [column.replace(
            "\r", " ") for column in columns]
        concatted_dataframe.columns = formatted_column_names[:-1]
        concatted_dataframe.to_excel(f"{name}", index=False)

    except Exception as e:
        sys.exit(f"...{str(e)}")


if __name__ == '__main__':
    pdf_path = 'Notification_Transmission charges for DICs_billing month_February_2023.pdf'
    table_to_find = "Transmission Charges for Designated ISTS Customers (DICs) for the billing month of"
    total_table_found = tables_finder(pdf_path, table_to_find)
    final_dataframe_maker(total_table_found)
