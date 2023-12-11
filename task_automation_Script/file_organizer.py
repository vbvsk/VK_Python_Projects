import os
import shutil

def organize_files(source_folder):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' not found.")
        return

    # Process each file in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Define destination folder based on the file extension
        destination_path = os.path.join(source_folder, extension[1:])

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Move the file to the destination folder
        shutil.move(source_path, os.path.join(destination_path, filename))
        print(f"Moved {filename} to {destination_path}")

if __name__ == "__main__":
    # Example usage - specify the Downloads folder or any other source folder
    source_folder = "/home/ckvb/Downloads/Telegram Desktop"

    organize_files(source_folder)

