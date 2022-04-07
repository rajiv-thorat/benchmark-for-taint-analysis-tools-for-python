import os

# This is for the output from the Snyk tool. The result is enclosed in single quotes, and there is a "b"
# at the begining that need to be removed for the string to be parsable as JSON.
def clean_stdout(stdout_raw:str):
    return stdout_raw[2:len(stdout_raw) - 1].replace("\\n", os.linesep)

def write_to_file(file_name:str, data_to_write:str):
    result_file = open(file_name, "w")
    result_file.write(data_to_write)