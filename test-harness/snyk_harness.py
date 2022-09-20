from asyncio.subprocess import PIPE
import json
import os
import subprocess
from sys import stdout

import utils
import logging
from os.path import abspath

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

class snyk_harness(Harness):
    harness_name = 'snyk'

    def run_tool(self):
        # Running docker over the entire test suite to save on the number of executions
        root_directory = abspath('..')
        command = ['docker', 'run', '--rm', '-it', '-e', 'SNYK_TOKEN=d9d5e2f6-430d-454a-8dd4-0c0fe4420552', '-v',  + f'{root_directory}:/app', '-v', f'{root_directory}/output:/op', 'snyk/snyk:python-3.8', 'snyk code test --json > /op/op.json']
        command_output = subprocess.run(command, stdout=PIPE, stderr=stdout, shell=False, universal_newlines=True)

    def read_result(self):
        output_directory = abspath('..') + '/output'
        do_comparison

def run_snyk_on_benchmark(test_parent, force_execution):
    for file in os.listdir(test_parent):
       project_root = os.path.join(test_parent, file)
       if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__" and file!= "resources"):
           run_snyk(project_root, force_execution)

def run_snyk(project_root, force_execution):
    snyk_result_file_path = os.path.join(utils.DIRECTORY_PATH_FOR_OUTPUT, project_root[project_root.rfind("/", 0, project_root.rfind("/")) + 1 :], utils.SNYK_RESULT_FILE)
    if(not os.path.exists(snyk_result_file_path) or force_execution):
        logging.info(f"Running Snyk code in {project_root}")
        #command = f"snyk code test --json {project_root}"
        # for some reason the --json-output-file does not generate the target file. 
        # Reading the stdout and cleaning it instead
        command = ["snyk", "code", "test", "--json", project_root]
        logging.debug(command)
        command_output = subprocess.run(command, stdout=PIPE, stderr=stdout, shell=False, universal_newlines=True)
        try:
            # Exit code is 0 if there are no issues detected. 
            # Return code is 1 if there are issues. Other codes are actual error codes
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code")
        utils.write_to_file(snyk_result_file_path, str(command_output.stdout))
    else:
        logging.info(f"The Snyk result already exists for {project_root}. Skipped execution.")
    
def read_results_and_compare():
    read_result(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS)
    read_result(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA)

def read_result(test_parent):
    for file in os.listdir(test_parent):
        project_root = os.path.join(test_parent, file)
        if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__" and file!="resources"):
            result = json.load(open(os.path.join(project_root, utils.SNYK_RESULT_FILE) , "r"))
            # taf = json.load(open(os.path.join(project_root, utils.TAF_FILE), "r"))
            # project_meta_data = json.load(open(os.path.join(project_root, utils.PROJECT_META_DATA), "r"))
            results = result["runs"][0]["results"]
            logging.debug(len(results))
    return results
