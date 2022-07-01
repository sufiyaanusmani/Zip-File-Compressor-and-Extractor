import os
from zipfile import ZipFile
from pathlib import Path
import time

while True:
    os.system("cls")
    print("1. Compress File")
    print("2. Extract File")
    print("3. Exit")
    choice = int(input("\nEnter your choice: "))

    # Compressing
    if choice == 1:
        os.system("cls")
        fileName = input("Enter file(with extension) or folder name: ")
        if Path(fileName).exists():
            if(Path(fileName).is_file()):
                with ZipFile("compressed.zip", "w") as zip:
                    zip.write(fileName)
            else:
                with ZipFile("compressed.zip", "w") as zip:
                    for path in Path(fileName).rglob("*.*"):
                        zip.write(path)
            os.system("cls")
            print("Compressed Successfully...")
            time.sleep(2)
        else:
            print("This file/folder does not exists")
            time.sleep(3)
    # Extracting
    elif choice == 2:
        os.system("cls")
        fileName = input("Enter name of compressed zip file: ")
        if ".zip" not in fileName:
            fileName = fileName + ".zip"
        
        if Path(fileName).exists():
            with ZipFile(fileName) as zip:
                zip.extractall("extracted")
                print("File extracted successfully...")
                time.sleep(2)
        else:
            print("This file does not exists")
            time.sleep(2)
    
    elif choice == 3:
        break

    else:
        os.system("cls")
        print("Please enter a valid choice")
        time.sleep(1)
