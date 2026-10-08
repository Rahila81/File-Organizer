# File Organizer

A simple Python automation tool that organizes files into separate folders based on their file extensions.

## Features

- Automatically organizes files
- Supports images, documents, code, audio, and video files
- Creates category folders automatically
- Moves unknown file types to an Other folder
- Supports preview mode before organizing
- Supports yes and no responses
- Validates user input
- Handles duplicate filenames safely
- Ignores existing folders
- Shows a final organization summary

## Categories

| File Type | Category |
|---|---|
| .jpg, .png, .jpeg | Images |
| .txt, .pdf, .docx | Documents |
| .py, .java, .c | Code |
| .mp3 | Audio |
| .mp4 | Videos |
| Other extensions | Other |

## How It Works

1. The user enters the folder path.
2. The program checks whether the folder exists.
3. The user can choose preview mode.
4. The program checks each file's extension.
5. A category is selected for each file.
6. Required category folders are created.
7. Files are moved into their respective folders.
8. Duplicate filenames are renamed safely.
9. A final summary is displayed.

## Requirements

- Python 3.x
- Windows, Linux, or macOS

## How to Run

1. Open the project folder in a terminal.
2. Run:

python organizer.py

3. Enter the folder path you want to organize.

Example:

Enter the folder path: C:\Users\Acer\Downloads

4. Choose whether you want preview mode.

## Example

Before organizing:

Downloads/
+-- photo.jpg
+-- resume.pdf
+-- program.py
+-- song.mp3
+-- unknown.xyz

After organizing:

Downloads/
+-- Images/
¦   +-- photo.jpg
+-- Documents/
¦   +-- resume.pdf
+-- Code/
¦   +-- program.py
+-- Audio/
¦   +-- song.mp3
+-- Other/
    +-- unknown.xyz

## Project Structure

File-Organizer/
+-- organizer.py
+-- README.md
+-- .gitignore

## Technologies Used

- Python
- os module
- shutil module

## Future Improvements

- Graphical User Interface
- Drag-and-drop support
- Undo organization
- More file categories
- Duplicate file detection
- File organization history
- Custom category configuration

## Author

Rahila S
