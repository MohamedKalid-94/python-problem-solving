"""
Phase 14 - Real World Python
Project 07 - File Organizer
Moves files into folders named after their extension (for example txt_files).
WARNING: do not run this on a folder that contains your own code.
"""

import os
import shutil


def get_folder_name(file):
    """Return the folder name for a file: 'photo.JPG' -> 'jpg_files'."""
    if "." in file:
        extension = file.rsplit(".", 1)[-1].lower()
        return extension + "_files"
    return "no_extension_files"


def organize_files(folder):
    """Move every file in the folder into a sub-folder. Returns how many were moved."""
    if not os.path.isdir(folder):
        print("Folder not found")
        return 0

    moved = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not os.path.isfile(path):      # skip sub-folders
            continue

        if file.startswith("."):          # skip hidden files like .gitignore
            continue

        new_folder = os.path.join(folder, get_folder_name(file))
        os.makedirs(new_folder, exist_ok=True)

        new_path = os.path.join(new_folder, file)

        if os.path.exists(new_path):      # never overwrite an existing file
            print(file, "Skipped (a file with this name is already there)")
            continue

        shutil.move(path, new_path)
        print(file, "Moved")
        moved += 1

    return moved


def main():
    folder = input("Folder Path: ").strip().strip('"')

    if not os.path.isdir(folder):
        print("Folder not found")
        return

    answer = input("Move all files in " + folder + "? (y/n): ").strip().lower()

    if answer != "y":
        print("Cancelled")
        return

    moved = organize_files(folder)
    print("Organization Completed.", moved, "files moved")


if __name__ == "__main__":
    main()