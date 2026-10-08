import shutil
import os

# Ask the user for the folder to organize
folder = input("Enter the folder path: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    exit()
# Ask whether the user wants preview mode
preview = input("Do you want to preview before organizing? (y/n): ").lower()

if preview not in ["y", "yes", "n", "no"]:
    print("Please enter y/yes or n/no.")
    exit()

# File extension → category mapping
categories = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".py": "Code",
    ".java": "Code",
    ".c": "Code",
    ".mp3": "Audio",
    ".mp4": "Videos"
}

# Get all files and folders inside the selected folder
files = os.listdir(folder)
if not any(os.path.isfile(os.path.join(folder, file)) for file in files):
    print("No files found to organize.")
    exit()


# Function to create a unique filename
def get_unique_filename(folder, filename):

    name, extension = os.path.splitext(filename)

    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = name + "_" + str(counter) + extension
        counter += 1

    return new_filename


# Preview mode
if preview in ["y", "yes"]:

    print()
    print("Preview:")

    for file in files:

        file_path = os.path.join(folder, file)

        # Ignore folders
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        if extension in categories:
            category = categories[extension]
        else:
            category = "Other"

        print(file, "→", category)

    print()

    confirm = input("Do you want to continue? (y/n): ").lower()

    if confirm not in ["y", "yes"]:
        print("Organization cancelled.")
        exit()


# Counters
moved_count = 0
category_count = {}


# Actual organization
for file in files:

    file_path = os.path.join(folder, file)

    # Ignore folders
    if not os.path.isfile(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()
    # Find category
    if extension in categories:
        category = categories[extension]
    else:
        category = "Other"

    # Create category folder path
    category_folder = os.path.join(folder, category)

    # Create category folder if it doesn't exist
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Source file
    source = os.path.join(folder, file)

    # Create unique filename if duplicate exists
    new_filename = get_unique_filename(category_folder, file)

    # Destination file
    destination = os.path.join(category_folder, new_filename)

    # Move the file
    shutil.move(source, destination)

    # Update counters
    moved_count += 1
    category_count[category] = category_count.get(category, 0) + 1

    print(file, "moved to", category)


# Final summary
print()
print("Organization completed!")
print("Files organized:", moved_count)

for category, count in category_count.items():
    print(category + ":", count)