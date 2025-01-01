import os

def add_numbering_to_folders():
    try:
        # Get the current working directory
        directory = os.getcwd()

        # Get all folders in the directory, excluding `.git`
        folders = [
            f for f in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, f)) and f != ".git"
        ]
        folders.sort()  # Sort folders alphabetically to ensure ascending order

        # Loop through folders and rename them with numbering
        for idx, folder in enumerate(folders, start=1):
            folder_path = os.path.join(directory, folder)
            # Create the new name with numbering
            new_name = f"{idx}.{folder}"
            new_folder_path = os.path.join(directory, new_name)
            
            # Rename the folder
            os.rename(folder_path, new_folder_path)
            print(f"Renamed: {folder} -> {new_name}")

        print("Numbering added to all folders successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to add numbering
add_numbering_to_folders()
