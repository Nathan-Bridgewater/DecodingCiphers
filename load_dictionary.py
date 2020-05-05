"""Load a text file in as a list.

Arguments:
- text file name (and path if needed)

Exceptions:
- FileNotFoundError

Returns:
-A list of all words in the text file in lowercase

requires import sys

"""
import sys


def load_file(file):
    """Open a text file and return a list of lowercase strings"""

    try:
        with open(file) as f:

            # Read the file, remove white space and split into a list
            loaded_text = f.read().strip().split()
            loaded_text = [x.lower() for x in loaded_text]

            return loaded_text

    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program",
              file=sys.stderr)
        sys.exit(1)
