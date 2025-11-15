import os

def sample_os_usage():
    # 1. Create a folder
    folder_name = "example_folder"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")

    # 2. Create a sample file inside it
    file_path = os.path.join(folder_name, "sample.txt")
    with open(file_path, "w") as f:
        f.write("This is a sample file created using the os library.\n")
    print(f"Created file: {file_path}")

    # 3. List all files in the folder
    print("Files in folder:", os.listdir(folder_name))

    # 4. Get absolute path of the file
    abs_path = os.path.abspath(file_path)
    print("Absolute path:", abs_path)

    # 5. Read environment variable
    home_dir = os.getenv("HOME", "Not Found")
    print("HOME environment variable:", home_dir)

    # 6. Clean up - delete file and folder
    os.remove(file_path)
    os.rmdir(folder_name)
    print("Cleaned up created files and folder.")

if __name__ == "__main__":
    sample_os_usage()
