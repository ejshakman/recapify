from pathlib import Path
from src.file_manager import move_files

if __name__ == "__main__":
    file_mappings = {
        "Marquee.json": "marquee.json",
        "Playlist1.json": "playlist.json",
        "YourLibrary.json": "library.json"
    }

    source_dir = "Spotify Account Data"
    target_dir = "data"

    move_files(source_dir, target_dir, file_mappings)
