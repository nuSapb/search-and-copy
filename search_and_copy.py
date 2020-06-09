import os, errno
import shutil
import pandas as pd
from pathlib import Path

def prepare_data(excel_file, target_column, target_file_type):
    df = pd.read_excel(excel_file)
    # print(df)
    serial_num = (df["Serial_Num"].astype(str) + target_file_type).tolist()
    # print(serial_num)
    return serial_num

def create_new_folder(destination_folder):
    if not os.path.exists(destination_folder):
        try:
            print("mkdir ", destination_folder)
            os.makedirs(destination_folder)
        except FileExistsError:
            pass

def search_and_copy(serial_num, source_folder, destination_folder):
    count_sn = 0
    target = destination_folder
    found = []
    exclude = set(["FAIL", "fail", "Fail"])
    for root, dirs, files in os.walk(data_folder):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith('.xls') and file in serial_num:
                # print(str(file))
                file_dir = Path(root) / file
                try:
                    shutil.copy(file_dir, target)
                    # print("The following file has been copied", file)
                    found.append(file)
                    count_sn += 1
                except shutil.SameFileError:
                    pass
            # else: print("no data")
    print("Total expected file: ",len(serial_num))
    print('Total file found: ', count_sn)
    file_not_found = list(set(serial_num) - set(found))

    if file_not_found:
        print("File not found below:")
        print(file_not_found)

if __name__ == "__main__":

    ########## Input data for test ##########
    source_folder = Path("D:/KETL/Product/Smith And Nephew/Trinity 4K/Test Results Record/91002021/New folder")
    destination_folder = source_folder / "RSN_1571"
    rsn_file = source_folder / "RSN# S&N 1571_Serial list.xlsx"
    target_column = "Serial_Num"
    target_file_type = ".xls"
    #########################################

    # source_folder = Path(input("Enter your source folder: "))
    # destination_folder = input("Enter your destination folder name: ")
    # rsn_file = input("Enter your RSN .xlsx file name: ")
    # target_column = input("Enter your serial number in RSN sheet column name: ")
    # target_file_type = input("Enter type of file you want to serch and copy: ")

    
    create_new_folder(destination_folder)
    data_folder = Path(source_folder)
    excel_file = data_folder / rsn_file
    serial_list = prepare_data(excel_file, target_column, target_file_type)
    search_and_copy(serial_list, source_folder, destination_folder)
