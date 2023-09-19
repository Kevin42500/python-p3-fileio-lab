# lib/testing/file_io_test.py
import os
from lib.file_io import write_file, append_to_file, read_file

def test_append_file(tmp_path):
    """Test append_file()"""
    
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "\nAppended content."
    
    # Use the temporary directory provided by pytest
    file_path = tmp_path / file_name
    write_file(file_path, file_content)
    
    # Use the correct function name 'append_to_file'
    append_to_file(file_path, append_content)
    
    # Check if the file exists in the temporary directory
    assert os.path.exists(file_path.with_suffix('.txt'))
    
    # Read the file and check its content
    with open(file_path.with_suffix('.txt'), 'r') as f:
        content = f.read()
        assert content.startswith(file_content)
        assert content.endswith(append_content)
