from subprocess import run
import logging
from harness import Harness
from pathlib import Path
import utils
from shutil import copy

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class SnykHarness(Harness):
    harness_name = 'snyk'
    SNYK_TOKEN = 'd9d5e2f6-430d-454a-8dd4-0c0fe4420552'

    def run_tool_on_directory(self, test_input_directory:Path):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        # docker run --rm -it -e "SNYK_TOKEN=d9d5e2f6-430d-454a-8dd4-0c0fe4420552" -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/abstract_factory_1:/app -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/snyk/abstract_factory_1:/op local/snyk-container
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-e', f'SNYK_TOKEN={self.SNYK_TOKEN}', 
        '-v', f'{test_input_directory.absolute().__str__()}:/app', 
        '-v', f'{self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__()}:/op', 
        'local/snyk-container']
        command_output = run(command)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. Snyk returns error code if vulnerabilities are found.")
        copy(test_input_directory.joinpath('.dccache').absolute().__str__(), self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__())

    def move_results(self, test_input_directory:Path):
        logging.info(f'Caching the results at {self.get_raw_output_dir_for_input_dir(test_input_directory).__str__()}.')
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('issues.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())

    def record_results(self, test_input_directory):
        files_to_look_for = utils.get_test_files_for_result_evaluation(test_directory)
        results = {}
        for file_to_look_for in files_to_look_for:
            results[file_to_look_for] = False
        #output_data = utils.read_json_file(Path('/home/rajiv/temp_/issues.json'))
        output_data = utils.read_json_file(self.get_ext_output_dir_for_input_dir(test_input_directory).joinpath('issues.json'))
        for vulnerability in output_data.get('runs')[0].get('results'):
            if vulnerability.get('ruleId') == 'python/CodeInjection':
                for file_to_look_for in files_to_look_for:
                    if file_to_look_for in vulnerability.get('locations')[0].get('physicalLocation').get('artifactLocation').get('uri'):
                        results[file_to_look_for] = True

        logging.info('Recording the results.')
        for result_key in results.keys():
            utils.write_to_csv_file(Path(f'{self.get_harness_type()}-result.csv'), [result_key, results.get(result_key)])

if __name__== '__main__':
    tool_harness_instance = SnykHarness()
    test_directory = Path('tests/synthetic_tests/if_statement_1')
    logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
    tool_harness_instance.make_output_directories(test_directory)
    tool_harness_instance.run_tool_on_directory(test_directory)
    tool_harness_instance.move_results(test_directory)
    tool_harness_instance.record_results(test_directory)