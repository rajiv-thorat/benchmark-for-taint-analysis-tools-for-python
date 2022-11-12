from harness import Harness
from snyk_harness import SnykHarness
from pysa_harness import PysaHarness
from codeql_harnesss import CodeQLHarness
from pyt_harness import PytHarness
import utils
from pathlib import Path
import logging
from non_exec_metrics_collector import NonExecMetricsCollector
from validator import Validator
from generate_metrics import GenerateMetrics

if __name__== '__main__':
    #Validator.do_validations()
    metrics_summary = {}
    for tool in Harness.__subclasses__():
        tool_harness_instance = tool()
        for test_directory in [x for x in utils.DIRECTORY_PATH_FOR_SYNTHETIC_TAINT_DATA.iterdir() if x.is_dir() and (x.name != 'experiments' or x.name != 'match_statement_1')]:
            if utils.DIRECTORY_FOR_RAW_OUTPUT.joinpath(tool_harness_instance.get_harness_type(), test_directory.name).exists():
                continue
            logging.info(f'Running {tool_harness_instance.get_harness_type()} on test {test_directory.name}.')
            tool_harness_instance.make_output_directories(test_directory)
            tool_harness_instance.run_tool_on_directory(test_directory)
            tool_harness_instance.move_results(test_directory)
            tool_harness_instance.record_results(test_directory)
        metrics_summary[tool_harness_instance.get_harness_type()] = GenerateMetrics.generate(tool_harness_instance.get_harness_type())
    
    coll = NonExecMetricsCollector()
    coll.collect()

    GenerateMetrics.write_metrics_summary(metrics_summary)    