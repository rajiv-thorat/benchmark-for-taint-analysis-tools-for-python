from asyncio.subprocess import PIPE
import subprocess

import logging
from os.path import abspath
from harness import Harness
from pathlib import Path
import requests
from time import sleep, time

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

class CodeQLHarness(Harness):
    harness_name = 'codeql'
    PATH_TO_THE_EXECUTION_SHELL_SCRIPT = 'test_harness/codeql_files/analyze_security.sh'

    def run_tool_on_directory(self, directory:Path):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement:/opt/src -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location:/opt/results -e CODEQL_CLI_ARGS="database analyze --format=csv --output=/opt/results/issues.csv /opt/results/source_db python-security-and-quality.qls" mcr.microsoft.com/cstsectools/codeql-container
        # sh test-harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location python
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location/source_db/results/codeql/python-queries/Security/CWE-078:/data -e CODEQL_CLI_ARGS="bqrs decode --format=csv -o /data/data.csv /data/CommandInjection.bqrs" mcr.microsoft.com/cstsectools/codeql-container 
        # docker build -t local/codeql -f ../dockerfile .
        # sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/with_statement_3 /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/codeql/with_statement_3 python
        check_github_api_status()
        command = ['sh', 
        PATH_TO_THE_EXECUTION_SHELL_SCRIPT,
        directory.absolute().__str__(), 
        self.get_raw_output_dir_for_input_dir(directory).absolute().__str__(), 
        'python']
        command_output = subprocess.run(command, stdout=PIPE, stderr=PIPE, shell=False, universal_newlines=True)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the CodeQL docker image.")

    def move_results(self):
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('issues.csv').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())
        for exec_metric_file_path in self.get_raw_output_dir_for_input_dir(directory).glob('*.txt'):
            copy(exec_metric_file_path.absolute().__str__(), 
            self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())
    
    def check_github_api_status(self):
        logging.info('Checking the API status of GitHub.')
        response = requests.get('https://api.github.com')
        remaining_calls = response.headers.get('x-ratelimit-remaining')
        calls_reset_at = response.headers.get('x-ratelimit-reset')
        logging.info(f'{remaining_calls} remaining API calls until {calls_reset_at}.')
        time_diff = int(calls_reset_at) - time()
        if int(remaining_calls) < 20:
            logging.info(f'Sleeping for {time_diff} seconds to let the GitHub API counter reset.')
            sleep(time_diff + 5)

if __name__== '__main__':
    tool_harness_instance = CodeQLHarness()
    for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and x.name != 'experiments']:
        logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
        tool_harness_instance.make_output_directories(test_directory)
        tool_harness_instance.run_tool_on_directory(test_directory)
        tool_harness_instance.move_results(test_directory)