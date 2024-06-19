# Manipulate Extended Streaming History JSON data.
# Remove entries for specified keys.
# Organize data into files by (type, year).
# Write in 'streaming_data/'.

import json
from collections import defaultdict
import os

# Function to remove specified keys from each entry
def remove_keys(entries, keys_to_remove):
    for entry in entries:
        for key in keys_to_remove:
            entry.pop(key, None)

# Define keys to remove from each entry
keys_to_remove = [
    "username", "platform", "ip_addr_decrypted",
    "user_agent_decrypted", "offline",
    "offline_timestamp", "incognito_mode"
]

# Directory containing JSON files
directory = 'extended_streaming_data/'

# Dictionary to hold split data by (type, year)
data_by_type_year = defaultdict(lambda: defaultdict(list))

# Process each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Determine type from filename
        if 'video' in filename.lower():
            data_type = 'video'
        elif 'audio' in filename.lower():
            data_type = 'audio'
        else:
            print(f"Unknown file type for file: {filename}")
            continue
        
        # Remove specified keys
        remove_keys(data, keys_to_remove)
        
        # Split data by year
        for entry in data:
            if 'ts' in entry:
                try:
                    year = entry['ts'][:4]  # Extract year from timestamp (assuming format is consistent)
                    data_by_type_year[data_type][year].append(entry)
                except ValueError:
                    print(f"Invalid timestamp format for entry in {filename}: {entry}")
            else:
                print(f"Timestamp 'ts' not found in entry in {filename}: {entry}")

# Create a folder for new JSON files if it doesn't exist
output_folder = 'streaming_data'
os.makedirs(output_folder, exist_ok=True)

# Write split data to separate JSON files for each type, year
for data_type, type_data in data_by_type_year.items():
    for year, entries in type_data.items():
        output_file_path = os.path.join(output_folder,f'streaming_history_{data_type}_{year}.json')
        with open(output_file_path, 'w') as f:
            json.dump(entries, f, indent=2)
        print(f"Data for {data_type} in year {year} written to {output_file_path}")