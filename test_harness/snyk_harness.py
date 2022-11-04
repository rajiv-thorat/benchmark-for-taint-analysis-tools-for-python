from asyncio.subprocess import PIPE
import subprocess

import logging
from os.path import abspath
from harness import Harness
from pathlib import Path
import utils
from shutil import copy

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

class SnykHarness(Harness):
    harness_name = 'snyk'
    SNYK_TOKEN = 'd9d5e2f6-430d-454a-8dd4-0c0fe4420552'

    def run_tool_on_directory(self, directory:Path):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        # docker run --rm -it -e "SNYK_TOKEN=d9d5e2f6-430d-454a-8dd4-0c0fe4420552" -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/abstract_factory_1:/app -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/snyk/abstract_factory_1:/op local/snyk-container
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-e', f'SNYK_TOKEN={self.SNYK_TOKEN}', 
        '-v', f'{directory.absolute().__str__()}:/app', 
        '-v', f'{self.get_raw_output_dir_for_input_dir(directory).absolute().__str__()}:/op', 
        'local/snyk-container']
        command_output = subprocess.run(command, stdout=PIPE, stderr=PIPE, shell=False, universal_newlines=True)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the Snyk docker image.")
        copy(directory.joinpath('.dccache').absolute().__str__(), self.get_raw_output_dir_for_input_dir(directory).absolute().__str__())

    def move_results(self, directory:Path):
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('issues.json').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())
        copy(self.get_raw_output_dir_for_input_dir(directory).joinpath('non_exec_metrics.txt').absolute().__str__(), 
        self.get_ext_output_dir_for_input_dir(directory).absolute().__str__())

if __name__== '__main__':
    tool_harness_instance = SnykHarness()
    for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and x.name != 'experiments']:
        logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
        tool_harness_instance.make_output_directories(test_directory)
        tool_harness_instance.run_tool_on_directory(test_directory)
        tool_harness_instance.move_results(test_directory)