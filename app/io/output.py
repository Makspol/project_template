import pandas as pd


def write_to_console(text):
    """
    A function for displaying text in the console.

    Note:
        Uses the standard print() method to print text to the console.

    Args:
        text (str): The text to be printed in the console.
    """
    print(text)


def write_file(text, path):
    """
    A function for writing text to a file with any extension.

    Note:
        The function uses built-in python capabilities to write to a file.

    Args:
        text (str): What you want to write to the file.
        path (str): The path to the file.
    """
    with open(path, 'w') as file:
        file.write(text)


def write_file_with_pandas(df, path):
    """
     The function writes lists, directories, etc. to a file.

     Note:
         Uses pandas to write data to .csv and .json files.

    Args:
        df (pd.DataFrame): Data to be written to a file (representing a table).
        path (str): The path to the file.
    """
    dot_name = path.split('.')[-1]

    if dot_name == 'csv':
        df.to_csv(path, index=False)
    elif dot_name == 'json':
        df.to_json(path)
