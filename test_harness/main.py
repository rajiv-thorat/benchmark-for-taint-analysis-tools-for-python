from harness import Harness
from snyk_harness import SnykHarness
from pysa_harness import PysaHarness
import utils
from os import path
import logging
from non_exec_metrics_collector import NonExecMetricsCollector

if __name__== '__main__':
    for tool in Harness.__subclasses__():
        tool_harness_instance = tool()
        for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and x.name != 'experiments']:
            logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
            tool_harness_instance.make_output_directories(test_directory)
            tool_harness_instance.run_tool_on_directory(test_directory)
            tool_harness_instance.move_results(test_directory)
            tool_harness_instance.record_results(test_directory)
    
    coll = NonExecMetricsCollector()
    coll.collect()