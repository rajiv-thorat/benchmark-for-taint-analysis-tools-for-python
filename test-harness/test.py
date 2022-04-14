from dataclasses import dataclass
import json
import logging
import utils
import re


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")
data = open("/Users/rajivthorat/Code/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/test.json", "r")
# data_clean = utils.clean_stdout(data.read())
# test = re.search(r"\"", data.read())
# for line in data.readlines():
    # print(line)
# logging.info(data_clean)
data_string = data.read()
json_data = json.loads(data_string)
print(str(len(json_data)))
# utils.write_to_file("/Users/rajivthorat/Code/MasterArbeit/submodules/benchmark-for-taint-analysis-tools-for-python/tests/test.json", data_clean)