# Import necessary libraries
import os  # Provides functions for interacting with the operating system
import shutil  # Allows file operations such as copying and moving

# Prompt the user to enter a path
path = input("Enter path: ")

# List all files in the specified directory
files = os.listdir(path)

# Loop through each file in the directory
for file in files:
    # Split the filename and its extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot (.) from the extension

    # Check if a directory with the extension name already exists
    if os.path.exists(path + '/' + extension):
        # If it exists, move the file into that directory
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        # If the directory does not exist, create it
        os.makedirs(path + '/' + extension)
        # Then, move the file into the newly created directory
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

#run the code , enter the path and enjoy! 