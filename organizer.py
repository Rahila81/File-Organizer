import shutil
import os


folder = input("Enter the folder path: ")

if not os.path.isdir(folder):
    print("Folder does not exist.")
    exit()

preview = input("Do you want to preview before organizing? (y/n): ").lower()

if preview not in ["y", "yes", "n", "no"]:
    print("Please enter y/yes or n/no.")
    exit()


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


files = os.listdir(folder)
if not any(os.path.isfile(os.path.join(folder, file)) for file in files):
    print("No files found to organize.")
    exit()



def get_unique_filename(folder, filename):

    name, extension = os.path.splitext(filename)

    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = name + "_" + str(counter) + extension
        counter += 1

    return new_filename



if preview in ["y", "yes"]:

    print()
    print("Preview:")

    for file in files:

        file_path = os.path.join(folder, file)

       
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



moved_count = 0
category_count = {}



for file in files:

    file_path = os.path.join(folder, file)

    
    if not os.path.isfile(file_path):
        continue

    
    extension = os.path.splitext(file)[1].lower()
   
    if extension in categories:
        category = categories[extension]
    else:
        category = "Other"

   
    category_folder = os.path.join(folder, category)


    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    
    source = os.path.join(folder, file)

   
    new_filename = get_unique_filename(category_folder, file)


    destination = os.path.join(category_folder, new_filename)

 
    shutil.move(source, destination)

    
    moved_count += 1
    category_count[category] = category_count.get(category, 0) + 1

    print(file, "moved to", category)



print()
print("Organization completed!")
print("Files organized:", moved_count)

for category, count in category_count.items():
    print(category + ":", count)
