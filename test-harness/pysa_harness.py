from harness import Harness

class PysaHarness(Harness):
    def run_tool_on_synthetic_tests(self):
        # pyre analyze --no-verify --save-results-to ./pysa-runs
        print('In the pysa harnss')