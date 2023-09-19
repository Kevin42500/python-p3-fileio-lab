# lib/file_io.py

def write_file(file_name, file_content):
    # Convert file_name to a string and add the .txt extension
    file_name = str(file_name) + ".txt"
    
    # Open the file in write mode and write the content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    # Convert file_name to a string and add the .txt extension
    file_name = str(file_name) + ".txt"
    
    # Open the file in append mode and append the content
    with open(file_name, 'a') as file:
        file.write("\n" + append_content)

def read_file(file_name):
    # Convert file_name to a string and add the .txt extension
    file_name = str(file_name) + ".txt"
    
    try:
        # Open the file in read mode and read the content
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {file_name} not found"
