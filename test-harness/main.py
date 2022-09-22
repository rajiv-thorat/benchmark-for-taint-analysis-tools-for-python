from harness import Harness
from snyk_harness import SnykHarness
from pysa_harness import PysaHarness

if __name__== '__main__':
    for tool in Harness.__subclasses__():
        tool_instance = tool()
        tool_instance.run_tool_on_synthetic_tests()