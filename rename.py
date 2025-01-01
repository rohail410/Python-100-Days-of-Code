import os
import re

def remove_numbering_from_folders():
    try:
        # Get the current working directory
        directory = os.getcwd()

        # Get all folders in the directory
        folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
        
        # Define a regex pattern to match numbered prefixes (e.g., "1.", "2.")
        pattern = re.compile(r"^\d+\.(.+)$")
        
        for folder in folders:
            folder_path = os.path.join(directory, folder)
            
            # Check if the folder name starts with a number and a dot
            match = pattern.match(folder)
            if match:
                # Extract the original name (everything after the number and dot)
                original_name = match.group(1)
                new_folder_path = os.path.join(directory, original_name)
                
                # Rename the folder
                os.rename(folder_path, new_folder_path)
                print(f"Renamed: {folder} -> {original_name}")

        print("All numbered prefixes removed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to remove numbering
remove_numbering_from_folders()
