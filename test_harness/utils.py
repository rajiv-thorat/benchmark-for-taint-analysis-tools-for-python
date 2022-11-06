import os
from pathlib import Path
import json
import csv

SNYK_RESULT_FILE = "snyk-result.json"
DIRECTORY_PATH_FOR_TESTS = "tests/"
DIRECTORY_PATH_FOR_OUTPUT = "output/"
DIRECTORY_PATH_FOR_OUTPUTS = {'codeql':'test_metadata/output_extracted/codeql', 'pysa':'test_metadata/output_extracted/pysa', 'snyk':'test_metadata/output_extracted/snyk'}

NON_EXEC_METRICS_SUMMARY_FILE = Path('non_exec_metrics_summary.csv')
DIRECTORY_FOR_RAW_OUTPUT = Path('test_metadata/outputs_raw')
DIRECTORY_FOR_EXTRACTED_OUTPUT = Path('test_metadata/output_extracted')
DIRECTORY_PATH_FOR_REALWORLD_PROJECTS = Path('tests/real-world-projects/')
DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA = Path('tests/synthetic_tests')
DIRECTORY_FOR_TEST_META_DATA = Path('test_metadata/synthetic_taint_data')
DIRECTORY_FOR_THE_PYT_PROJECT = Path('test_harness/pyt_files/docker_build/pyt')

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

def read_json_file(file_location:Path):
    with file_location.open() as opened_file:
        json_data = json.load(opened_file)
    return json_data

def read_csv_file(file_location:Path):
    with file_location.open() as opened_file:
        csv_file = csv.reader(opened_file)
        csv_data = [line for line in csv_file]
    return csv_data

if __name__ == '__main__':
    read_csv_file(Path('/home/rajiv/temp_/issues.csv'))
    read_json_file(Path('/home/rajiv/temp_/vuls.json'))