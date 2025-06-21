import os
from google.genai import types


def write_file(working_directory, file_path, content):
    real_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.abspath(real_file_path).startswith(
        os.path.abspath(working_directory)
    ):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    directory = os.path.dirname(real_file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(real_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes specified content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file we want to write content into",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we want to write into the file provided in file_path",
            ),
        },
    ),
)
