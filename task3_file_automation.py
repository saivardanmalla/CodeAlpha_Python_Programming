# Task 3: Move JPG Files Automatically

import os
import shutil

# Source folder containing images
source_folder = "Images"

# Destination folder
destination_folder = "JPG_Files"


# Check whether source folder exists
if not os.path.exists(source_folder):
    print("Images folder not found!")
    exit()


# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)


# Get all files from Images folder
files = os.listdir(source_folder)


# Move only JPG files
for file in files:

    if file.lower().endswith(".jpg"):

        old_path = os.path.join(source_folder, file)
        new_path = os.path.join(destination_folder, file)

        shutil.move(old_path, new_path)

        print(file, "moved successfully")


print("\n✅ All JPG files moved successfully!")