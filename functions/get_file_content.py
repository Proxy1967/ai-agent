import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    real_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.abspath(real_file_path).startswith(
        os.path.abspath(working_directory)
    ):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(real_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(real_file_path, "r") as f:
            file_content_string = f.read()

        if len(file_content_string) > MAX_CHARS:
            return (
                file_content_string[:MAX_CHARS]
                + f'[...File "{file_path}" truncated at 10000 characters]'
            )

        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Prints out the content of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file whose content we want to print out",
            ),
        },
    ),
)
