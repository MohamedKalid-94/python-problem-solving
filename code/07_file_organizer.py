# Phase 14 - Real World Python
# Project 07 - File Organizer

import os
import shutil

def organize_files(folder):
    for file in os.listdir(folder):
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            ext=file.split(".")[-1]
            new_folder=os.path.join(folder,ext)
            os.makedirs(new_folder,exist_ok=True)
            shutil.move(path,os.path.join(new_folder,file))
            print(file,"Moved")

def main():
    folder=input("Folder Path: ")
    organize_files(folder)
    print("Organization Completed")

if __name__=="__main__": main()