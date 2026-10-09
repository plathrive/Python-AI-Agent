import os, subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute python file with optional arguments in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to get file content from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "list[string]",
                    "description": "List of directory or file that extend to command variable which will be pass to subprocess method, relative to the working directory (default is the working directory itself) and the file path",
                },
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if valid_target_dir != True:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]

        if args != None:
            command.extend(args)

        running_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=30)

        if running_process.returncode != 0:
            return f"Process exited with code {running_process.returncode}"
    
        elif running_process.stdout == "" and running_process.stderr == "":
            return "No output produced"

        else:
            result = f"STDOUT: {running_process.stdout}\nSTDERR: {running_process.stderr}"
            return result    

    except Exception as e:
        return f"Error: executing Python file {e}"