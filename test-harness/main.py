from harness import Harness
from snyk_harness import SnykHarness
from pysa_harness import PysaHarness

if __name__== '__main__':
    for tool in Harness.__subclasses__():
        tool_harness_instance = tool()
        tool_harness_instance.run_tool_on_synthetic_tests()
        #tool_harness_instance.run_tool_on_real_world_tests()
        tool_harness_instance.compare_results()