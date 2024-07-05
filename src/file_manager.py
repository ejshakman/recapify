import shutil
from pathlib import Path
import json


def move_files(source_dir, target_dir, file_mappings):
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    # Create target directory if it does not exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Move files from source directory to target directory with new names
    for original_name, new_name in file_mappings.items():
        source_file = source_dir / original_name
        target_file = target_dir / new_name

        if source_file.exists():
            shutil.move(source_file, target_file)
        else:
            raise FileNotFoundError(f"Source file {source_file} not found.")


# def rename_and_move_file(source_dir_path, dest_dir_path, new_name):
#     source_dir = Path(source_dir_path)
#     destination_dir = Path(destination_dir_path)


# def modify_entries(directory, keys_to_remove):
#     directory_path = Path(directory)
#     keys_to_remove = {
#     ''
# }

#     for file_path in directory_path.glob('*.json'):
#         with open(file_path, 'r') as file:
#             data = json.load(file)

#     for key in keys_to_remove:
#         if key in data:
#             del data[key]

#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)