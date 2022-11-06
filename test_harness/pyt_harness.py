from harness import Harness
import logging
from pathlib import Path
import utils
from subprocess import run
from shutil import copy

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class PytHarness(Harness):
    harness_name = 'pyt'
    def run_tool_on_directory(self, test_input_directory:Path):
        # docker run --rm -it -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/pyt_files/docker_build/pyt:/pyt -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_tests/if_statement_1:/app python:3.8-buster sh
        # docker run --rm -it -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_tests/if_statement_1:/app -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/pyt_files/docker_build/pyt:/pyt -v /home/rajiv/temp_:/op local/pyt-container        
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-v', f'{test_input_directory.absolute().__str__()}:/app', 
        '-v', f'{utils.DIRECTORY_FOR_THE_PYT_PROJECT.absolute().__str__()}:/pyt',
        '-v', f'{self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__()}:/op', 
        'local/pyt-container']
        command_output = run(command)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. Pyt returns an error code when issues are found.")

    def move_results(self, test_input_directory):
        logging.info(f'Caching the results at {self.get_raw_output_dir_for_input_dir(test_input_directory).__str__()}.')
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('vuls.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(test_input_directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(test_input_directory).absolute().__str__())

    def record_results(self, test_input_directory):
        files_to_look_for = self.get_test_files_for_result_evaluation(test_directory)
        results = {}
        for file_to_look_for in files_to_look_for:
            results[file_to_look_for] = False
        output_data = utils.read_json_file(self.get_ext_output_dir_for_input_dir(test_input_directory).joinpath('vuls.json'))
        #output_data = utils.read_json_file(Path('/home/rajiv/temp_/vuls.json'))
        for vulnerability in output_data.get('vulnerabilities'):
            if vulnerability.get('sink_trigger_word') == 'eval(':
                for file_to_look_for in files_to_look_for:
                    if file_to_look_for in vulnerability.get('sink').get('path'):
                        results[file_to_look_for] = True
                        
        logging.info('Recording the results.')
        for result_key in results.keys():
            utils.write_to_csv_file(Path(f'{self.get_harness_type()}-result.csv'), [result_key, results.get(result_key)])

if __name__== '__main__':
    tool_harness_instance = PytHarness()
    test_directory = Path('tests/synthetic_tests/if_statement_1')
    logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
    tool_harness_instance.make_output_directories(test_directory)
    tool_harness_instance.run_tool_on_directory(test_directory)
    tool_harness_instance.move_results(test_directory)
    tool_harness_instance.record_results(test_directory)