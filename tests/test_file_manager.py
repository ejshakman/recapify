import os
import pytest
import shutil
import json
from src.file_manager import split_files, delete_directory

@pytest.fixture(scope="module")
# Set up test environment
def setup_test_env(tmpdir):
    test_dir = tmpdir.mkdir("test_env")

    # Create test JSON files
    for i in range(3):
        file_path = test_dir.join(f"test_file_{i}.json")
        with open(file_path, 'w') as f:
            json.dump({"key": f"value_{i}"}, f)

    # Create a subdirectory with files
    sub_dir = test_dir.mkdir("sub_dir")
    with open(sub_dir.join("test_file_3.json"), 'w') as f:
        json.dump({"key": "value_3"}, f)

    return test_dir

def test_split_files(setup_test_env):
    test_dir = setup_test_env

    # Call the function
    split_files(test_dir)

    # Assert files are broken up correctly
    for i in range(3):
        assert not test_dir.join(f"test_file_{i}.json").check()
        assert test_dir.join(f"new_test_file_{i}.json").check()

def test_delete_directory(setup_test_env):
    test_dir = setup_test_env

    # Call the function
    delete_directory(test_dir)

    # Assert directory is deleted
    assert not test_dir.check()
    # Assert backup directory exists
    assert os.path.exists("backup_dir")
    shutil.rmtree("backup_dir")  # Cleanup after test