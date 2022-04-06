import json
import os
import subprocess
import utils


def run_benchmark_on_snyk(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
    for file in os.listdir(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS):
        project_root = DIRECTORY_PATH_FOR_REALWORLD_PROJECTS + file
        if(os.path.isdir(project_root)):
            run_snyk(project_root)

    for file in os.listdir(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
        project_root = os.path.join(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, file)
        if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__"):
            run_snyk(project_root)
            break

def run_snyk(project_root):
    print(f"Running Snyk code in {project_root}")
    #command = f"snyk code test --json {project_root}"
    result_file_location = os.path.join(project_root, "snyk-result.json")
    # for some reason the --json-output-file does not generate the target file. 
    # Reading the stdout and cleaning it instead
    command_output = subprocess.run(["snyk", "code", "test", "--json", project_root], capture_output=True)
    print(command_output.args)
    command_output.check_returncode()
    utils.write_to_file(os.path.join(project_root, "snyk-result.json"), utils.clean_stdout(str(command_output.stdout)))
    
