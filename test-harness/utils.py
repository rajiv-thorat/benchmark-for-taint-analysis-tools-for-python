from black import NewLine


def clean_stdout(stdout_raw:str):
    print(stdout_raw)
    return stdout_raw.replace("\n", NewLine)

def write_to_file(file_name:str, data_to_write:str):
    result_file = open(file_name, "w")
    result_file.write(data_to_write)