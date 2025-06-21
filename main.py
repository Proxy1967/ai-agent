import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions
from functions.call_function import call_function

MAX_ITERATIONS = 20


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("Wrong input")
        print('Use: python3 main.py "your prompt here" [--verbose]')
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # generate_response(client, messages, user_prompt, verbose)

    iterations = 0

    while True:
        iterations += 1

        if iterations > MAX_ITERATIONS:
            print(f"Maximum iterations of {MAX_ITERATIONS} reached.")
            sys.exit(1)

        try:
            response = generate_response(client, messages, verbose)
            if response:
                print(f"Response: {response}")
                break
        except Exception as e:
            print(f"Error generating a response: {e}")


def generate_response(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()
