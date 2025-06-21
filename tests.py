from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
import os


def test():

    print(run_python_file("calculator", "main.py"))
    print("")

    print(run_python_file("calculator", "tests.py"))
    print("")

    print(run_python_file("calculator", "../main.py"))
    print("")

    print(run_python_file("calculator", "nonexistent.py"))

    # print(
    #     write_file(
    #         "calculator",
    #         os.path.join("calculator", "lorem.txt"),
    #         "wait, this isn't lorem ipsum",
    #     )
    # )
    # print(
    #     write_file(
    #         "calculator",
    #         os.path.join("calculator", "pkg/morelorem.txt"),
    #         "lorem ipsum dolor sit amet",
    #     )
    # )
    # print(
    #     write_file(
    #         "calculator",
    #         os.path.join("calculator", "/tmp/temp.txt"),
    #         "this should not be allowed",
    #     )
    # )

    # print(get_file_content("calculator", os.path.join("calculator", "lorem.txt")))
    # print("")
    # print(get_file_content("calculator", os.path.join("calculator", "main.py")))
    # print("")
    # print(
    #     get_file_content("calculator", os.path.join("calculator", "pkg/calculator.py"))
    # )
    # print("")
    # print(get_file_content("calculator", os.path.join("calculator", "/bin/cat")))
    # print("")

    # print(get_files_info("calculator", os.path.join("calculator", ".")))
    # print("")
    # print(get_files_info("calculator", os.path.join("calculator", "pkg")))
    # print("")
    # print(get_files_info("calculator", os.path.join("calculator", "/bin")))
    # print("")
    # print(get_files_info("calculator", os.path.join("calculator", "../")))


if __name__ == "__main__":
    test()
