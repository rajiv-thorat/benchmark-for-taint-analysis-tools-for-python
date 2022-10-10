from asyncio.subprocess import PIPE
import subprocess

import logging
from os.path import abspath
from harness import Harness

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

class CodeQLHarness(Harness):
    harness_name = 'codeql'

    def run_tool_on_synthetic_tests(self):
        # Running docker over the synthetic and real world tests in a single execution to keep the number of runs to a minimum.
        logging.info('Running CodeQL.')
        root_directory = abspath('..')
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement:/opt/src -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location:/opt/results -e CODEQL_CLI_ARGS="database analyze --format=csv --output=/opt/results/issues.csv /opt/results/source_db python-security-and-quality.qls" mcr.microsoft.com/cstsectools/codeql-container
        # sh test-harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location python
        # docker run --rm --name codeql-container -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs/temp_codeql_db_location/source_db/results/codeql/python-queries/Security/CWE-078:/data -e CODEQL_CLI_ARGS="bqrs decode --format=csv -o /data/data.csv /data/CommandInjection.bqrs" mcr.microsoft.com/cstsectools/codeql-container 
        # sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_harness/codeql_files/analyze_security.sh /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/with_statement_3 /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/codeql/with_statement_3 python
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