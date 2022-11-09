from harness import Harness
import logging
from pathlib import Path
import utils
from subprocess import run, STDOUT, PIPE
from shutil import copy

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class PysaHarness(Harness):
    DIRECTORY_PATH_FOR_PYSA_CONFIG = Path('test_harness/pysa_files/pysa_config')
    harness_name = 'pysa'
    def run_tool_on_directory(self, test_input_directory:Path):
        # inside docker container:
        # pyre init-pysa
        # pyre analyze --no-verify --save-results-to ./pysa-runs
        # time -o /op/non_exec_metrics.txt pyre analyze --no-verify --save-results-to /op 
        # docker run --rm -it -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/pysa_files/pysa_config:/config -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/with_statement_1:/code -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/pysa/with_statement_1:/op local/pysa
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-v', f'{self.DIRECTORY_PATH_FOR_PYSA_CONFIG.absolute()}:/config', 
        '-v', f'{test_input_directory.absolute().__str__()}:/code', 
        '-v', f'{self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__()}:/op', 
        'local/pysa']
        command_output = run(command)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the Pysa docker image.")

    def move_results(self, test_input_directory):
        logging.info(f'Caching the results at {self.get_raw_output_dir_for_input_dir(test_input_directory).__str__()}.')
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('errors.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())

    def record_results(self, test_input_directory):
        files_to_look_for = utils.get_test_files_for_result_evaluation(test_input_directory)
        results = {}
        for file_to_look_for in files_to_look_for:
            results[file_to_look_for] = False
        #output_data = utils.read_json_file(Path('/home/rajiv/temp_/errors.json'))
        output_data = utils.read_json_file(self.get_ext_output_dir_for_input_dir(test_input_directory).joinpath('errors.json'))
        for vulnerability in output_data:
            if vulnerability.get('code') == 5001:
                for file_to_look_for in files_to_look_for:
                    if file_to_look_for in vulnerability.get('define'):
                        results[file_to_look_for] = True

        logging.info('Recording the results.')
        for result_key in results.keys():
            utils.write_to_csv_file(Path(f'{self.get_harness_type()}-result.csv'), [result_key, results.get(result_key)])

if __name__== '__main__':
    tool_harness_instance = PysaHarness()
    test_directory = Path('tests/synthetic_tests/if_statement_1')
    logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
    tool_harness_instance.make_output_directories(test_directory)
    tool_harness_instance.run_tool_on_directory(test_directory)
    tool_harness_instance.move_results(test_directory)
    tool_harness_instance.record_results(test_directory)