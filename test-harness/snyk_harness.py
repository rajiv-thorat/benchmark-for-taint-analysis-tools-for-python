import json
import os
import subprocess


def run_benchmark_on_snyk(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
    for file in os.listdir(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS):
        project_root = DIRECTORY_PATH_FOR_REALWORLD_PROJECTS + file
        if(os.path.isdir(project_root)):
            run_snyk(project_root)

    for file in os.listdir(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
        project_root = os.path.join(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, file)
        if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__"):
            run_snyk(project_root)

def run_snyk(project_root):
    print(f"Running Snyk code in {project_root}")
    #command = f"snyk code test --json {project_root}"
    result_file_location = os.path.join(project_root, "snyk-result.json")
    command_output = subprocess.run(["snyk", "code", "test", "--json", f"--json-file-output={result_file_location}", project_root])
    print(command_output.args)
    command_output.check_returncode()
    #result_file = open(os.path.join(project_root, "snyk-result.json"), "w")
    #result_file.write(str(command_output.stdout))