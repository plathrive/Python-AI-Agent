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
            listing_directory = os.listdir(target_dir)
            result_list = []

            for obj in listing_directory:
                absolute_obj = os.path.abspath(os.path.join(target_dir, obj))
                result_list.append(f"- {obj}: file_size={os.path.getsize(absolute_obj)} bytes, is_dir={os.path.isdir(absolute_obj)}")
            
            result = "\n".join(result_list)
            return result

    except FileNotFoundError:
        return "File not found error: Please check your directories!"
    except Exception as e:
        return e