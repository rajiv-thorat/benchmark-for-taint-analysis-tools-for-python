from harness import Harness
import logging
from pathlib import Path
import utils

class PysaHarness(Harness):
    DIRECTORY_PATH_FOR_PYSA_CONFIG = Path('test_harness/pysa_files/pysa_config')
    harness_name = 'pysa'
    def run_tool_on_directory(self, directory:Path):
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
        '-v', f'{directory.absolute().__str__()}:/code', 
        '-v', f'{self.get_raw_output_dir_for_input_dir(directory).absolute().__str__()}:/op', 
        'local/pysa']
        command_output = subprocess.run(command, stdout=PIPE, stderr=PIPE, shell=False, universal_newlines=True)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the Pysa docker image.")

    def move_results(self):
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('errors.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())