import os
import shutil

def organize_files(source_folder):
    # Create a dictionary to map file extensions to their respective folders
    extensions_folders = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'xlsx': 'Spreadsheets',
        # Add more file types and their corresponding folders as needed
    }

    # Create folders for each file type
    for folder in extensions_folders.values():
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

    # Organize files
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_extension = filename.split('.')[-1]
            if file_extension in extensions_folders:
                source_path = os.path.join(source_folder, filename)
                destination_folder = extensions_folders[file_extension]
                destination_path = os.path.join(source_folder, destination_folder, filename)

                # Move the file to its respective folder
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {destination_folder} folder.")

# Replace 'source_folder' with the path to the directory you want to organize
source_folder = 'C:/Users/acer/OneDrive/Desktop/File Organizer'#path_to/dir_of/your_working_dir...
organize_files(source_folder)