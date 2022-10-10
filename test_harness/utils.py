import os
from black import Path

TAF_FILE = "taf.json"
PROJECT_META_DATA = "meta-data.json"
SNYK_RESULT_FILE = "snyk-result.json"
DIRECTORY_PATH_FOR_REALWORLD_PROJECTS = "tests/real-world-projects/"
DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA = "tests/synthetic-taint-data/"
DIRECTORY_PATH_FOR_TESTS = "tests/"
DIRECTORY_PATH_FOR_OUTPUT = "output/"

# This is for the output from the Snyk tool. The result is enclosed in single quotes, and there is a "b"
# at the begining that need to be removed for the string to be parsable as JSON.
def clean_stdout(stdout_raw:str):
    return stdout_raw[2:len(stdout_raw) - 1].replace("\\n", os.linesep).replace("\\'", "'").replace("\\\"","\"").replace("\\\n", "\n")

def write_to_file(file_name:str, data_to_write:str):
    # Create the directory if it does not exist.
    directory = Path(os.path.dirname(file_name))
    directory.mkdir(parents=True, exist_ok=True)
    # The actual write
    result_file = open(file_name, "w+")
    result_file.write(data_to_write)