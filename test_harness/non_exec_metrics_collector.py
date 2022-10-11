import utils
from os import listdir, path
from numpy import average

class NonExecMetricsCollector:
    def collect(self):
        summary = {}
        for tool_name in utils.DIRECTORY_PATH_FOR_OUTPUTS.keys():
            summary[tool_name] = []
            for directory in listdir(utils.DIRECTORY_PATH_FOR_OUTPUTS.get(tool_name)):
                total_metrics_for_test = {
                'total_execution_time': 0.0 ,
                'max_mem_usage_in_kb' : '',
                'no_of_file_system_inputs' : 0,
                'no_of_file_system_outputs' : 0
            }
                for op_file in listdir(utils.DIRECTORY_PATH_FOR_OUTPUTS.get(tool_name) + path.sep + directory):
                    if op_file.endswith('.txt'):
                        current_file_data = self.parse_non_exec_metric_file(utils.DIRECTORY_PATH_FOR_OUTPUTS.get(tool_name) + path.sep + directory + path.sep + op_file)
                        total_metrics_for_test['total_execution_time'] = total_metrics_for_test['total_execution_time'] + current_file_data['total_execution_time']
                        total_metrics_for_test['max_mem_usage_in_kb'] = str(total_metrics_for_test['max_mem_usage_in_kb']) + ',' + str(current_file_data['max_mem_usage_in_kb'])
                        total_metrics_for_test['no_of_file_system_inputs'] = str(total_metrics_for_test['no_of_file_system_inputs']) + ',' + str(current_file_data['no_of_file_system_inputs'])
                        total_metrics_for_test['no_of_file_system_outputs'] = str(total_metrics_for_test['no_of_file_system_outputs']) + ',' + str(current_file_data['no_of_file_system_outputs'])
                total_metrics_for_test['max_mem_usage_in_kb'] = average(
                [int(n) for n in str(total_metrics_for_test['max_mem_usage_in_kb'])[1:].split(',')])
                
                summary.get(tool_name).append({
                    directory : total_metrics_for_test
                })
                print('test')

    def parse_non_exec_metric_file(self, op_file):
        with open(op_file) as non_exec_metric_file:
            lines = non_exec_metric_file.readlines()
            if lines.__contains__('Command exited with non-zero status 1'):
                first_line = lines[1]
                second_line = lines[2]
            else:
                first_line = lines[0]
                second_line = lines[1]
            line_leftover = first_line.split('user')
            user_space_time_in_sec = float(line_leftover[0].strip())
            line_leftover = line_leftover[1].split('system')
            system_space_time_in_sec = float(line_leftover[0].strip())
            line_leftover = line_leftover[1].split('elapsed')
            elapsed_time_split = line_leftover[0].strip().split(':')
            elapsed_time_mins = elapsed_time_split[0]
            elapsed_time_secs = elapsed_time_split[1]
            total_elapsed_time_in_sec = float(elapsed_time_mins) * 60 + float(elapsed_time_secs)
            line_leftover = line_leftover[1].split('maxresident)k')
            line_leftover = line_leftover[0].split(' ')
            max_mem_usage_in_kb = int(line_leftover[line_leftover.__len__() - 1])
            line_leftover = second_line.split('inputs')
            no_of_file_system_inputs = int(line_leftover[0])
            line_leftover = line_leftover[1].split('outputs')
            no_of_file_system_outputs = int(line_leftover[0][1:])
            return {
                'total_execution_time': user_space_time_in_sec + system_space_time_in_sec + total_elapsed_time_in_sec ,
                'max_mem_usage_in_kb' : max_mem_usage_in_kb,
                'no_of_file_system_inputs' : no_of_file_system_inputs,
                'no_of_file_system_outputs' : no_of_file_system_outputs
            }



if __name__=='__main__':
    coll = NonExecMetricsCollector()
    coll.collect()