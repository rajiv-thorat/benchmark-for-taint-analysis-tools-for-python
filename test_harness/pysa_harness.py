from harness import Harness

class PysaHarness(Harness):
    def run_tool_on_synthetic_tests(self):
        # inside docker container:
        # pyre init-pysa
        # pyre analyze --no-verify --save-results-to ./pysa-runs
        # time -o /op/non_exec_metrics.txt pyre analyze --no-verify --save-results-to /op 
        # docker run --rm -it -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test-harness/pysa_files/pysa_config:/config -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic_taint_data/if_statement_1:/code -v /home/rajiv/git/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/test_metadata/outputs_raw/pysa/if_statement_1:/op local/pysa
        print('In the pysa harnss')