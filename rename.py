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
        
        # Sort folders alphabetically to ensure proper order
        folders.sort()

        # Loop through folders and rename them with numbering and leading zeros
        for idx, folder in enumerate(folders, start=1):
            folder_path = os.path.join(directory, folder)
            # Create the new name with numbering and leading zeros (e.g., 01, 02, 03)
            new_name = f"{idx:02d}.{folder}"  # Number with leading zeros
            new_folder_path = os.path.join(directory, new_name)
            
            # Rename the folder
            os.rename(folder_path, new_folder_path)
            print(f"Renamed: {folder} -> {new_name}")

        print("Numbering added to all folders successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to add numbering
add_numbering_to_folders()
