from abc import ABC
import abc
from pathlib import Path
import utils
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class Harness(ABC):
    harness_name = 'Unimplemented'

    def get_harness_type(self):
        return self.harness_name

    @abc.abstractmethod
    def run_tool_on_directory(self, test_input_directory:Path):
       ... 

    @abc.abstractmethod
    def move_results(self, test_input_directory:Path):
        ...

    def make_output_directories(self, test_input_direcory:Path):
        logging.info('Creating the output directories.')
        utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), test_input_direcory.name).mkdir(parents=True)
        utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), test_input_direcory.name).mkdir(parents=True)
    
    def get_raw_output_dir_for_input_dir(self, test_input_directory:Path):
        return utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), test_input_directory.name)
    
    def get_ext_output_dir_for_input_dir(self, test_input_directory:Path):
        return utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), test_input_directory.name)

    @abc.abstractmethod
    def record_results(self, test_input_directory:Path):
        ...

    """ @abc.abstractmethod
    def compare_results(self):
        ... """
