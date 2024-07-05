import pytest
import shutil
from pathlib import Path
import json
from src.file_manager import move_files


# Create test environment with directories and files
@pytest.fixture
# Define paths
def setup_test_environment():
    # Setup directories and files for testing
    source_dir = Path("SourceDir")
    target_dir = Path("TargetDir")

    source_dir.mkdir(parents=True, exist_ok=True)
    target_dir.mkdir(parents=True, exist_ok=True)

    # Create example data
    data_audio = [
            {
                "ts": "2022-12-01T21:41:58Z",
                "delete_all": "delete from all",
                "delete_audio": "delete from audio",
                "delete_video": "delete from video",
            },
            {
                "ts": "2024-12-01T21:41:59Z",
                "delete_all": "delete from all",
                "delete_audio": "delete from audio",
                "delete_video": "delete from video",
            }
        ]
    data_video = [
        {
            "ts": "2022-11-01T21:41:58Z",
            "delete_all": "delete from all",
            "delete_audio": "delete from audio",
            "delete_video": "delete from video",
        },
        {
            "ts": "2024-11-01T21:41:59Z",
            "delete_all": "delete from all",
            "delete_audio": "delete from audio",
            "delete_video": "delete from video",
        }
        ]
    data_rename_move = [
        {
            "foo": "bar",
            "delete_all": "delete from all"
        }
    ]


    # Write data to files
    (source_dir / 'Marquee.json').write_text(json.dumps(data_audio, indent=2))
    (source_dir / 'Playlist1.json').write_text(json.dumps(data_video, indent=2))
    (source_dir / 'YourLibrary.json').write_text(json.dumps(data_rename_move, indent=2))


    # Define new file names to be used in move_files test
    file_mappings = {
        "Marquee.json" : "marquee.json",
        "Playlist1.json" : "playlist.json",
        "YourLibrary.json": "library.json"
    }

    # Pass parameters to be used in tests
    yield source_dir, target_dir, file_mappings

    # Teardown after tests
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)


'''
TC-01 move_files
Inputs: SourceDir, TargetDir, file mappings
Output: Specified files from source should be in target under new names
'''
def test_move_files(setup_test_environment):
    # Pull values from setup_test_environment
    source_dir, target_dir, file_mappings = setup_test_environment

    move_files(source_dir, target_dir, file_mappings)

    # Assert that files are moved and renamed correctly
    for original_name, new_name in file_mappings.items():
        source_file = source_dir / original_name
        target_file = target_dir / new_name

        assert not source_file.exists(), (f"{original_name} should be removed from SourceDir.")
        assert target_file.exists(), (f"{original_name} should be in TargetDir as {new_name}.")

    # Verify data in new file matches data from old file
    with target_file.open() as f:
        data = json.load(f)
        expected_data = [{
            "foo": "bar",
            "delete_all": "delete from all"
            }]
        assert data == expected_data, f"Content of {new_name} does not match expected."


'''
TC-02 split_data
Inputs: dir w/ files w/ entries with different ts vals and comb of audio/video type
Output: new files created for each combo and placed in a new dir
'''

'''
TC-03 delete_dir
Inputs: dir path
Output: dir path and contents deleted
'''

'''
TC-04 remove_keys
Inputs: dir w/ files w/ entries w/ keys to remove
Output: entries in dir should have keys removed and others should still there
'''

'''
TC-05 remove_keys_by_type
Inputs: dir w/ files of audio and video type w/ entries w/ keys to remove
Output: entries in files should have respective keys removed and others still there
'''