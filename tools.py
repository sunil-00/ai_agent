from langchain_core.tools import tool

@tool
def write_code_to_file(code: str) -> str:
    """Write code to example.py file at specified path (code).

    Args:
        code (str): Code to write to file.

    Returns:
        str: Success message.
    """
    file_path = "./example.py"
    with open(file_path, 'w') as f:
        f.write(code)
    return f"Code successfully written to {file_path}."

@tool
def append_code_to_file(code: str) -> str:
    """Append code to example.py file at specified path (code).

    Args:
        code (str): The code to be appended.

    Returns:
        str: A success message indicating that the code was successfully appended.
    """
    file_path = "./example.py"
    with open(f"./{file_path}", 'a') as f:
        f.write(code)
    return f"Code successfully appended to {file_path}."

@tool
def read_code_from_file() -> str:
    """Read code from example.py file.

    Returns:
        str: The contents of the file.
    """
    file_path = "./example.py"
    code = None
    with open(file_path, 'r') as f:
        code = f.read()
    return code

__all__ = [
    'write_code_to_file',
    'append_code_to_file',
    'read_code_from_file',
]
