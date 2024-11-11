# import os

# # Base path to your dataset folder
# base_path = 'D:/CAPSTONEPROJECT/CropDataset'

# # List of subdirectories to process (Train, Test, Val)
# subdirs = ['train', 'test', 'val']

# # Loop through each subdirectory
# for subdir in subdirs:
#     subdir_path = os.path.join(base_path, subdir)
    
#     # Loop through all subdirectories and files within the current subdirectory
#     for root, dirs, files in os.walk(subdir_path):
#         for filename in files:
#             # Check if the filename has trailing whitespace
#             if filename != filename.rstrip():
#                 # Get the full path of the original and new filename
#                 original_path = os.path.join(root, filename)
#                 new_filename = filename.rstrip()  # Remove trailing whitespace
#                 new_path = os.path.join(root, new_filename)

#                 # Rename the file
#                 os.rename(original_path, new_path)
#                 print(f'Renamed: {original_path} to {new_path}')

# print("Renaming complete. All filenames now have trailing whitespace removed.")



# import os

# # Base path to your dataset folder
# base_path = 'D:/CAPSTONEPROJECT/CropDataset'

# # List of subdirectories to process (Train, Test, Val)
# subdirs = ['train', 'test', 'val']

# # Loop through each subdirectory
# for subdir in subdirs:
#     subdir_path = os.path.join(base_path, subdir)
    
#     # Loop through all subdirectories and files within the current subdirectory
#     for root, dirs, files in os.walk(subdir_path):
#         for filename in files:
#             # Check if the filename has trailing whitespace or hidden characters
#             if filename != filename.rstrip() or filename != filename.strip():
#                 # Get the full path of the original and new filename
#                 original_path = os.path.join(root, filename)
#                 new_filename = filename.strip()  # Remove trailing and leading whitespace
#                 new_path = os.path.join(root, new_filename)

#                 try:
#                     # Rename the file
#                     os.rename(original_path, new_path)
#                     print(f'Renamed: {original_path} to {new_path}')
#                 except OSError as e:
#                     print(f'Error renaming {original_path}: {e}')

# print("Renaming complete. All filenames now have trailing/leading whitespace and hidden characters removed.")



import os

# Base path to your dataset folder
base_path = 'D:/CAPSTONEPROJECT/CropDataset'

# List of subdirectories to process (Train, Test, Val)
subdirs = ['train', 'test', 'val']
count = 0
# Loop through each subdirectory
for subdir in subdirs:
    subdir_path = os.path.join(base_path, subdir)
    print(subdir_path)
    # Loop through all subdirectories and files within the current subdirectory
    for root, dirs, files in os.walk(subdir_path):
        for filename in files:
            count+=1
            print(filename)
            # Check if the filename contains any whitespace
            if " " in filename:
                # Get the full path of the original and new filename
                original_path = os.path.join(root, filename)
                new_filename = filename.replace(" ", "")  # Remove all whitespace from the filename
                new_path = os.path.join(root, new_filename)

                try:
                    # Rename the file
                    os.rename(original_path, new_path)
                    print(f'Renamed: {original_path} to {new_path}')
                except OSError as e:
                    print(f'Error renaming {original_path}: {e}')

print("Renaming complete. All filenames now have all whitespace removed.")
print(f"Total files = {count}")

