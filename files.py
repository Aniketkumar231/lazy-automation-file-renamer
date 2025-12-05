def rename_files(folder_path, prefix):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg'):
            new_name = prefix + filename
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
                count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
    
    print(f"Total files renamed: {count}")
