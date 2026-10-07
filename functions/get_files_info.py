import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if valid_target_dir != True:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir == True:
            return f'Success: "{directory}" is within the working directory'

    except ValueError:
        return "Value error: Please check your values!"
    except TypeError:
        return "Type error: Please check your types!"
    except FileNotFoundError:
        return "File not found error: Please check your directories!"
    except Exception as e:
        return e