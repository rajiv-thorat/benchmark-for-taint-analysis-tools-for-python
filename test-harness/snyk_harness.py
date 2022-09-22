from asyncio.subprocess import PIPE
import subprocess

import logging
from os.path import abspath
from harness import Harness

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

class SnykHarness(Harness):
    harness_name = 'snyk'

    def run_tool_on_synthetic_tests(self):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        logging.info('Running Snyk code.')
        root_directory = abspath('..')
        # docker run --rm -it -e "SNYK_TOKEN=d9d5e2f6-430d-454a-8dd4-0c0fe4420552" -v $(pwd):/app snyk/snyk:python-3.8 snyk code test --json > new.json
        command = ['docker', 'run', '--rm', '-it', '-e', 'SNYK_TOKEN=d9d5e2f6-430d-454a-8dd4-0c0fe4420552', '-v',  + f'{root_directory}:/app', '-v', f'{root_directory}/output:/op', 'snyk/snyk:python-3.8', 'snyk code test --json > /op/op.json']
        command_output = subprocess.run(command, stdout=PIPE, stderr=PIPE, shell=False, universal_newlines=True)
        logging.info(f'Finished executing {command_output.args}')
        try:
            command_output.check_returncode()
        except:
            logging.error(f"The subprocess returned {command_output.returncode} code. There was a problem running the Snyk docker image.")


    def read_result(self):
        output_directory = abspath('..') + '/output'
        do_comparison

    def make_results_comparable(self):
        logging.info('Making the results comparable.')
