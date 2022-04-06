import json
import utils

data = open("/Users/rajivthorat/Code/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/synthetic-taint-data/src/compound-statements/for-statement/snyk-result.json", "r")
data_clean = utils.clean_stdout()
utils.write_to_file("test.json", data)