import os
import shutil
import time

source_folder = "source_folder"
destination_folder = "destination_folder"

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mov"],
    "archives": [".zip", ".rar", ".tar"],
}

for folder in file_types.keys():
    folder_path = os.path.join(destination_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_files_by_type():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination_path = os.path.join(destination_folder, folder, filename)
                    shutil.move(file_path, destination_path)
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(destination_folder, "others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved {filename} to others")

def delete_old_files(days=30):
    current_time = time.time()
    for folder_name, extensions in file_types.items():
        folder_path = os.path.join(destination_folder, folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_age = (current_time - os.path.getmtime(file_path)) / (24 * 3600)
                if file_age > days:
                    os.remove(file_path)
                    print(f"Deleted {filename} (older than {days} days)")

def delete_large_files(size_mb=100):
    for folder_name, extensions in file_types.items():
        folder_path = os.path.join(destination_folder, folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                if file_size_mb > size_mb:
                    os.remove(file_path)
                    print(f"Deleted {filename} (larger than {size_mb} MB)")

move_files_by_type()
delete_old_files(days=30)
delete_large_files(size_mb=100)