import pandas as pd


def read_line_from_console(message):
    """
    Function for reading from the console.

    Note:
        The function uses the standard input() method to read from the console.

    Args:
        message (str): The message you want to display before reading
            the string into the console.

    Returns:
        (str): A line from the console.
    """
    return input(message)


def read_file(path):
    """
    A function for reading a file.

    Note:
        The function uses built-in python capabilities to read a file.

    Args:
        path (str): The path to the file.

    Returns:
        (str): Data from a file.
    """
    with open(path) as file:
        data = file.read()
    return data


def read_file_with_pandas(path):
    """
    Function for reading .csv and .json files.

    Note:
        The function uses the pandas library.

    Args:
        path (str): The path to the file.

    Returns:
        (pd.DataFrame): Data from a file that represents a table.
        Returns None if the path points to a file other than .csv and .json.
    """
    dot_name = path.split('.')[-1]
    data = None

    if dot_name == 'csv':
        data = pd.read_csv(path)
    elif dot_name == 'json':
        data = pd.read_json(path)
    return data
