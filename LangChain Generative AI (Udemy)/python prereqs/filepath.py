import os

# new_directory = "test_dir2"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created")

## Listing Files And Directories
items = os.listdir('.')
print(items)

## Joining Paths 
dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name, file_name)
print(full_path)
full_path = os.path.join(os.getcwd(), dir_name, file_name)
print(full_path)

path = 'example1.txt'
if os.path.exists(path):
    print(f"The path '{path}' exists.")
else:
    print(f"The path '{path}' does not exist.")
    
# Checking if a path is a file or a directory
path = 'AI/LangChain Generative AI (Udemy)/example.txt'
if os.path.isfile(path):
    print('Is a file')
elif os.path.isdir(path):
    print('Is a directory')
else:
    print ('Is neither')
    
## Getting Absolute Path
relative_path = 'AI/LangChain Generative AI (Udemy)/example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)