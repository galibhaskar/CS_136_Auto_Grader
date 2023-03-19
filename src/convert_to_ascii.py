# @Author: SashaChernykh
# @Date: 2018-09-01 13:31:06
# @Last Modified time: 2018-09-01 14:39:30
"""kira_encoding module."""
import codecs
import chardet
import sys
from unidecode import unidecode


def kira_encoding_function(filename):
    """Check encoding and convert to UTF-8, if encoding not UTF-8."""

    # Not 100% accuracy:
    # https://stackoverflow.com/a/436299/5951529
    # Check:
    # https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function
    # https://stackoverflow.com/a/37531241/5951529
    with open(filename, "rb") as opened_file:
        bytes_file = opened_file.read()
        chardet_data = chardet.detect(bytes_file)
        fileencoding = chardet_data["encoding"]
        print("fileencoding", fileencoding)

        if fileencoding in ["ascii"]:
            print(filename + " in ascii encoding")
        else:
            # Convert file to UTF-8:
            # https://stackoverflow.com/a/191403/5951529
            with codecs.open(filename, "r") as file_for_conversion:
                read_file_for_conversion = file_for_conversion.read()
            # Strip or replace unicode characters
            neutral_ascii_file = unidecode(read_file_for_conversion)
            # Write as ASCII
            with codecs.open(filename, "w", "ascii") as converted_file:
                converted_file.write(neutral_ascii_file)
            print(
                filename
                + " in "
                + fileencoding
                + " encoding automatically converted to ASCII "
            )


kira_encoding_function(sys.argv[1])
