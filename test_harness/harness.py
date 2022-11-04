from abc import ABC
import abc
from pathlib import Path

class Harness(ABC):
    harness_name = 'Unimplemented'

    @abc.abstractmethod
    def get_harness_type(self):
        return self.harness_name

    @abc.abstractmethod
    def run_tool_on_directory(self, directory:Path):
        raise NotImplementedError('Please implement before use.')

    @abc.abstractmethod
    def move_results(self):
        raise NotImplementedError('Please implement before use.')

    def make_output_directories(self, directory:Path):
        """ if not utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type()).exists():
            utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type()).mkdir()
        if not utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type()).exists():
            utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type()).mkdir() """
        if not utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), directory).exists():
            utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(self.get_harness_type(), directory).mkdir()
        if not utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), directory).exists():
            utils.DIRECTORY_FOR_EXTRACTED_OUTPUT.joinpath(self.get_harness_type(), directory).mkdir()
    
    def make_results_comparable(self):
        raise NotImplementedError('Please implement before use.')

    def compare_results(self):
        raise NotImplementedError('Please implement before use.')