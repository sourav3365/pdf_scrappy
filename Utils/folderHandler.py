import os
import sys
import shutil


def create_folder(folder_name="downloads"):
    '''
    @author : Sourav Choudhury
    @Params : folder_name - The folder name to be created in the current directory

    @Job    : Create the folder in the current directory.
    '''
    try:
        path_to_check = os.getcwd()+f"\\{folder_name}"
        if os.path.exists(path_to_check):
            print('...Downloads folder found')
            shutil.rmtree(path_to_check)
            os.mkdir("downloads")
        else:
            print('...Creating downloads folder in the current directory')
            os.mkdir("downloads")
    except Exception as e:
        sys.exit(f"{str(e)}")


def get_file_from_folder(path="download"):
    '''
    @author : Sourav Choudhury
    @Params : folder_name - The folder name to be created in the current directory

    @Job    : Create the folder in the current directory.
    '''
    try:
        return os.listdir(path)[0]
    except Exception as e:
        sys.exit(f"{str(e)}")
