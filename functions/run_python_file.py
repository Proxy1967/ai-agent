import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path):
    real_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.abspath(real_file_path).startswith(
        os.path.abspath(working_directory)
    ):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(real_file_path):
        return f'Error: File "{file_path}" not found'

    if not real_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            args=["python3", real_file_path],
            capture_output=True,
            timeout=30,
            cwd=os.path.abspath(working_directory),
        )

        if not result.stdout and not result.stderr:
            return "No output produced."

        if result.returncode != 0:
            return f"STDOUT: {result.stdout.decode()}\nSTDERR: {result.stderr.decode()}\nProcess exited with code {result.returncode}"
        else:
            return f"STDOUT: {result.stdout.decode()}\nSTDERR: {result.stderr.decode()}"

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file we want to run",
            ),
        },
    ),
)
