import os
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")

    function_dict = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    if function_call_part.name in function_dict:
        function_call_part.args["working_directory"] = "./calculator"
        result = function_dict[function_call_part.name](**function_call_part.args)

        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
