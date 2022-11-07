from jsonschema import validate
from pathlib import Path
import requests
import json
import utils
import logging
from subprocess import run, PIPE, TimeoutExpired

taf_schema = json.loads(requests.get('https://raw.githubusercontent.com/TaintBench/TaintBench/master/TAF-schema.json').text)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

class Validator:
    @staticmethod
    def do_validations():
        logging.info('Begining TAF file validations.')
        for test_directory in utils.DIRECTORY_FOR_TEST_META_DATA.iterdir():
            for taf_file in test_directory.glob('*_taf.json'):
                Validator.validate_taf_file(taf_file)
        logging.info('Begining test validations.')
        for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and x.name != 'experiments']:
            for test_file_name in utils.get_test_files_for_result_evaluation(test_directory):
                Validator.validate_test(test_directory.joinpath(test_file_name + '.py'))
            

    @staticmethod
    def validate_setup():
        # check for the docker containers
        raise NotImplementedError()

    @staticmethod
    def validate_taf_file(file_location:Path):
        logging.info(f'Validating {file_location.name}.')
        taf_file = utils.read_json_file(file_location)
        validate(taf_file, taf_schema)

    @staticmethod
    def validate_test(test_file:Path):
        logging.info(f'Validating {test_file.name}.')
        command = ['docker', 
        'run', 
        '--rm', 
        #'-it', 
        '-v', f'{test_file.absolute().__str__()}:/app/{test_file.name}', 
        'local/flask']
        try:
            command_output = run(command, stderr=PIPE, stdin=PIPE, stdout=PIPE, timeout=1)
            command_output.check_returncode()
        except TimeoutExpired:
            logging.info(f'The test {test_file.name} can run.') 
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code for test {test_file.name}.")

if __name__ == '__main__':
    #Validator.validate_taf_file(Path('test_metadata/synthetic_taint_data/abstract_factory_1/abstract_factory_1_actual_taf.json'))
    #Validator.validate_test(Path('tests/synthetic_tests/minimal_test_1/minimum_test_1_actual.py'))
    #for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and x.name != 'experiments']:
    #        test_files = utils.get_test_files_for_result_evaluation(test_directory)
    Validator.do_validations()