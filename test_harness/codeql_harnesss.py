from subprocess import run
import logging
from harness import Harness
from pathlib import Path
import requests
from time import sleep, time
import utils
from shutil import copy

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class CodeQLHarness(Harness):
    harness_name = 'codeql'
    PATH_TO_THE_EXECUTION_SHELL_SCRIPT = 'test_harness/codeql_files/analyze_security.sh'

    def run_tool_on_directory(self, test_input_directory:Path):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement:/opt/src -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location:/opt/results -e CODEQL_CLI_ARGS="database analyze --format=csv --output=/opt/results/issues.csv /opt/results/source_db python-security-and-quality.qls" mcr.microsoft.com/cstsectools/codeql-container
        # sh test-harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location python
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location/source_db/results/codeql/python-queries/Security/CWE-078:/data -e CODEQL_CLI_ARGS="bqrs decode --format=csv -o /data/data.csv /data/CommandInjection.bqrs" mcr.microsoft.com/cstsectools/codeql-container 
        # docker build -t local/codeql -f ../dockerfile .
        # sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/with_statement_3 /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/codeql/with_statement_3 python
        self.check_github_api_status()
        command = ['sh', 
        self.PATH_TO_THE_EXECUTION_SHELL_SCRIPT,
        test_input_directory.absolute().__str__(), 
        self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__(), 
        'python']
        command_output = run(command)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the CodeQL docker image.")

    def move_results(self, test_input_directory):
        logging.info(f'Caching the results at {self.get_raw_output_dir_for_input_dir(test_input_directory).__str__()}.')
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('issues.csv').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())
        for exec_metric_file_path in self.get_raw_output_dir_for_input_dir(test_input_directory).glob('*.txt'):
            copy(exec_metric_file_path.absolute().__str__(), 
            self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())

    def record_results(self, test_input_directory):
        files_to_look_for = self.get_test_files_for_result_evaluation(test_directory)
        results = {}
        for file_to_look_for in files_to_look_for:
            results[file_to_look_for] = False
        #output_data = utils.read_csv_file(Path('/home/rajiv/temp_/issues.csv'))
        output_data = utils.read_csv_file(self.get_ext_output_dir_for_input_dir(test_input_directory).joinpath('issues.csv'))
        for vulnerability in output_data:
            if vulnerability[0] =='Code injection' :
                for file_to_look_for in files_to_look_for:
                    if file_to_look_for in vulnerability[4]:
                        results[file_to_look_for] = True

        logging.info('Recording the results.')
        for result_key in results.keys():
            utils.write_to_csv_file(Path(f'{self.get_harness_type()}-result.csv'), [result_key, results.get(result_key)])

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
    test_directory = Path('tests/synthetic_tests/if_statement_1')
    logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
    tool_harness_instance.make_output_directories(test_directory)
    tool_harness_instance.run_tool_on_directory(test_directory)
    tool_harness_instance.move_results(test_directory)
    tool_harness_instance.record_results(test_directory)