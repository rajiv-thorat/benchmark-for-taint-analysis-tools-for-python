class Harness:
    harness_name = 'Unimplemented'

    def get_harness_type(self):
        return self.harness_name

    def run_tool_on_synthetic_tests(self):
        raise NotImplementedError('Please implement before use.')

    def read_results(self):
        raise NotImplementedError('Please implement before use.')
    
    def make_results_comparable(self):
        raise NotImplementedError('Please implement before use.')

    def compare_results(self):
        raise NotImplementedError('Please implement before use.')