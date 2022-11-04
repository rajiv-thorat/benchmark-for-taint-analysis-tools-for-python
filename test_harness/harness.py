from abc import ABC
import abc
from pathlib import Path
import utils

class Harness(ABC):
    harness_name = 'Unimplemented'

    def get_harness_type(self):
        return self.harness_name

    @abc.abstractmethod
    def run_tool_on_directory(self, directory:Path):
       ... 

    @abc.abstractmethod
    def move_results(self):
        ...

    def make_output_directories(self, directory:Path):
        """ if not utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type()).exists():
            utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type()).mkdir()
        if not utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type()).exists():
            utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type()).mkdir() """
        if not utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), directory.name).exists():
            utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), directory.name).mkdir()
        if not utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), directory.name).exists():
            utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), directory.name).mkdir()
    
    def get_raw_output_dir_for_input_dir(self, directory:Path):
        return utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), directory.name)
    
    def get_ext_output_dir_for_input_dir(self, directory:Path):
        return utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), directory.name)

    def make_results_comparable(self):
        raise NotImplementedError('Please implement before use.')

    def compare_results(self):
        raise NotImplementedError('Please implement before use.')