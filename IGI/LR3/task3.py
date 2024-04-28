def is_binary_string(s):
    """
    Check if a string is a binary string.

    Args:
        s (str): The string to be checked.

    Returns:
        bool: True if the string is a binary string, False otherwise.
    """
    return all(c in '01' for c in s)

def print_str(s):
    print(is_binary_string(s))

