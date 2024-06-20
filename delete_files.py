# Delete files in "Spotify Account Data/" that will not be used:
#     "Follow.json", "Identifiers.json", "Identity.json", "Inferences.json",
#     "Payments.json", "SearchQueries.json", "Userdata.json"

import json
import os

# If "Spotify Account Data/Follow.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Follow.json"):
    os.remove("Spotify Account Data/Follow.json")
    print("Spotify Account Data/Follow.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Follow.json " + "file not found")


# If "Spotify Account Data/Identifiers.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Identifiers.json"):
    os.remove("Spotify Account Data/Identifiers.json")
    print("Spotify Account Data/Identifiers.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Identifiers.json " + "file not found")


# If "Spotify Account Data/Identity.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Identity.json"):
    os.remove("Spotify Account Data/Identity.json")
    print("Spotify Account Data/Identity.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Identity.json " + "file not found")


# If "Spotify Account Data/Inferences.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Inferences.json"):
    os.remove("Spotify Account Data/Inferences.json")
    print("Spotify Account Data/Inferences.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Inferences.json " + "file not found")


# If "Spotify Account Data/Payments.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Payments.json"):
    os.remove("Spotify Account Data/Payments.json")
    print("Spotify Account Data/Payments.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Payments.json " + "file not found")


# If "Spotify Account Data/SearchQueries.json" file exists, delete it.
if os.path.exists("Spotify Account Data/SearchQueries.json"):
    os.remove("Spotify Account Data/SearchQueries.json")
    print("Spotify Account Data/SearchQueries.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/SearchQueries.json " + "file not found")


# If "Spotify Account Data/Userdata.json" file exists, delete it.
if os.path.exists("Spotify Account Data/Userdata.json"):
    os.remove("Spotify Account Data/Userdata.json")
    print("Spotify Account Data/Userdata.json deleted.")
else:
    # If it fails, inform the user.
    print("Error: " + "Spotify Account Data/Userdata.json " + "file not found")