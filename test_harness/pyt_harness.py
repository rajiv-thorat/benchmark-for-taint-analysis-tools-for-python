from harness import Harness
import logging
from pathlib import Path
import utils

class PytHarness(Harness):
    harness_name = 'pyt'
    def run_tool_on_directory(self, test_input_directory:Path):
        # inside docker container:
        # docker run --rm -it -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_tests/if_statement_1:/app -v /home/rajiv/temp_:/op local/pyt-container
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-v', f'{test_input_directory.absolute().__str__()}:/app', 
        '-v', f'{self.get_raw_output_dir_for_input_dir(test_input_directory).absolute().__str__()}:/op', 
        'local/pyt-container']
        command_output = subprocess.run(command)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the Pysa docker image.")

    def move_results(self):
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('vuls.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())

if __name__== '__main__':
    tool_harness_instance = PytHarness()
    test_directory = Path('tests/synthetic_tests/if_statement_1')
    logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
    tool_harness_instance.make_output_directories(test_directory)
    tool_harness_instance.run_tool_on_directory(test_directory)
    tool_harness_instance.move_results(test_directory)
    tool_harness_instance.get_test_files_for_result_evaluation(test_directory)