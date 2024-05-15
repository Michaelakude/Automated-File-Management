# Overview

This script organizes and sorts pictures and videos from a specified source directory into a target directory based on their date information extracted from the filenames on Windows. The files are moved into subfolders named by year and month.

# Functionality

List Files: It lists all the filed in the specified source directory.

Exclude Files: Allows the user to specify files that should not be moved.

Date Extraction: It extracts the date from the filenames using a regular expression.

Folder Organisation: It creates folders based on the extracted year and month.

Move Files: It moves the files to the appropiate folders in the target directory.

Handle Duplicates: Handles Duplicates by checking their sizes and either deleting or notifying the user of different sizes.

# Why This Approach

It is useful for quality of life, as it automates the very tedious task of organising files manually. It ensures a consistent folder structure for easy navigation and retrieval. It is flexible as it allowes users to specify files not be moved. It prevents duplication of files and manages identical files efficiently.

# How to Use

Source Directory: Set the source variable to the path of the directory containing the files you want to organize.

Target Directory: Set the target variable to the path of the directory where you want the organized files to be moved.

File Extensions: The EXTENSIONS list contains the file extensions of the files you want to organize (e.g., jpg, png, mp4).

Date Pattern: The DATE_PATTERN regular expression is used to extract the year and month from the filenames.

Exclude Files: Input the names of files you want to exclude from being moved when prompted.

# Conclusion

This script is designed to simplify and automate the process of organizing your pictures and videos by date. By using this script, you can save time and maintain a well-organized directory structure for your media files.
