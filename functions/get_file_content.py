import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get and read file contents in a specified directory relative to the working directory, truncated at max characters at 10000",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to get file content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if valid_target_dir != True:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file "{file_path}"'

        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            content = file_content_string
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    
    except FileNotFoundError:
        return "Error: The file couldn't be found!"
    except UnicodeDecodeError:
        return "Error: It's not a correct encoder!"
    except PermissionError:
        return "Error: You're not permissible to read this file!"
