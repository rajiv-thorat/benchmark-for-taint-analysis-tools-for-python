from asyncio.subprocess import PIPE
import json
import os
import subprocess
from sys import stderr, stdout
import utils
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
def run_benchmark_on_snyk(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, DIRECTORY_PATH_FOR_TESTS):
    #for file in os.listdir(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS):
    #    project_root = os.path.join(DIRECTORY_PATH_FOR_REALWORLD_PROJECTS, file)
    #    if(os.path.isdir(project_root)):
    #        run_snyk(project_root)
    #logging.info("Finished running Snyk Code on the real world projects.")

    #for file in os.listdir(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA):
    #    project_root = os.path.join(DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA, file)
    #    if(os.path.isdir(project_root) and file != ".DS_Store" and file!= "__pycache__"):
    #        run_snyk(project_root)
    #logging.info("Finished running Snyk Code on the synthetic tests.")
    run_snyk(DIRECTORY_PATH_FOR_TESTS)
    logging.info("Finished running snyk on the project.")

def run_snyk(project_root):
    logging.info(f"Running Snyk code in {project_root}")
    #command = f"snyk code test --json {project_root}"
    result_file_location = os.path.join(project_root, "snyk-result.json")
    # for some reason the --json-output-file does not generate the target file. 
    # Reading the stdout and cleaning it instead
    command = ["snyk", "code", "test", "--json", project_root]
    logging.debug(command)
    command_output = subprocess.run(command, stdout=PIPE, stderr=stdout, shell=False, universal_newlines=True)
    try:
        # For some reason the exit code is 1.
        command_output.check_returncode()
    except:
        logging.error(f"The subprocess returned {command_output.returncode} code")
    utils.write_to_file(os.path.join(project_root, "snyk-result-raw"), str(command_output.stdout))
    utils.write_to_file(result_file_location, utils.clean_stdout(str(command_output.stdout)))
    
