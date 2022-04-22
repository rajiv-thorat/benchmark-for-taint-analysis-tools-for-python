from asyncio.subprocess import PIPE
import json
import os
import subprocess
from sys import stderr, stdout
from unittest import result
import utils
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
def run_benchmark_on_snyk():
    for file in os.listdir(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS):
       project_root = os.path.join(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, file)
       if(os.path.isdir(project_root)):
           run_snyk(project_root)
    logging.info("Finished running Snyk Code on the real world projects.")

    for file in os.listdir(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
       project_root = os.path.join(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, file)
       if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__"):
           run_snyk(project_root)
    logging.info("Finished running Snyk Code on the synthetic tests.")
    # run_snyk(DIRECTORY_PATH_FOR_TESTS)
    # logging.info("Finished running snyk on the project.")

def run_snyk(project_root):
    logging.info(f"Running Snyk code in {project_root}")
    #command = f"snyk code test --json {project_root}"
    result_file_location = os.path.join(project_root, utils.SNYK_RESULT_FILE)
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
    # utils.write_to_file(os.path.join(project_root, "snyk-result-raw_"), str(command_output.stdout))
    utils.write_to_file(result_file_location, str(command_output.stdout))
    
def read_results_and_compare():
    for file in os.listdir(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS):
        project_root = os.path.join(utils.DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, file)
        if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__" and file!="resources"):
            result = json.load(open(os.path.join(project_root, utils.SNYK_RESULT_FILE) , "r"))
            # taf = json.load(open(os.path.join(project_root, utils.TAF_FILE), "r"))
            # project_meta_data = json.load(open(os.path.join(project_root, utils.PROJECT_META_DATA), "r"))
            results = result["runs"][0]["results"]
            logging.debug(len(results))



    for file in os.listdir(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
       project_root = os.path.join(utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, file)
       if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__" and file!="resources"):
            result = json.load(open(os.path.join(project_root, utils.SNYK_RESULT_FILE) , "r"))
            # taf = json.load(open(os.path.join(project_root, utils.TAF_FILE), "r"))
            # project_meta_data = json.load(open(os.path.join(project_root, utils.PROJECT_META_DATA), "r"))
            results = result["runs"][0]["results"]
            logging.debug(len(results))
