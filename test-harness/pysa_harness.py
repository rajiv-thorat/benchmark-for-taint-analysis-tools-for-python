from harness import Harness

class PysaHarness(Harness):
    def run_tool_on_synthetic_tests(self):
        # inside docker container:
        # pyre init-pysa
        # pyre analyze --no-verify --save-results-to ./pysa-runs
        print('In the pysa harnss')