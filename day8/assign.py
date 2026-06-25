#write a python script that performs file organisation of your downlaod folder 
#code logic for file automation
import os
import shutil

# Path to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Python Files": [".py"],
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(downloads_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# Create an "Others" folder
others_folder = os.path.join(downloads_folder, "Others")
os.makedirs(others_folder, exist_ok=True)

# Organize files
for file in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file)
    extension = extension.lower()

    moved = False

    # Check file type and move
    for folder, extensions in file_types.items():
        if extension in extensions:
            shutil.move(file_path, os.path.join(downloads_folder, folder, file))
            print(f"Moved: {file} -> {folder}")
            moved = True
            break

    # Move unknown files to Others
    if not moved:
        shutil.move(file_path, os.path.join(others_folder, file))
        print(f"Moved: {file} -> Others")

print("\nDownloads folder has been organized successfully!")