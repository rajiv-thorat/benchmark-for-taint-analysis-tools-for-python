import utils
from pathlib import Path
from csv import writer

class GenerateMetrics:
    @staticmethod
    def generate(tool_name):
        metrics = {
            'TP' : 0,
            'FP' : 0,
            'FN' : 0,
            'precision': 0.0,
            'recall': 0.0,
            'f_score': 0.0
        }
        results = utils.read_csv_file(Path(tool_name  + '-result.csv'))
        for result in results:
            if result[0].__contains__('sanitized') and result[1] == 'True':
                metrics['FP'] = metrics.get('FP') + 1
            if result[0].__contains__('false_positive') and result[1] == 'True':
                metrics['FP'] = metrics.get('FP') + 1
            if result[0].__contains__('actual') and result[1] == 'True':
                metrics['TP'] = metrics.get('TP') + 1
            if result[0].__contains__('actual') and result[1] == 'False':
                metrics['FN'] = metrics.get('FN') + 1
        metrics['precision'] = metrics.get('TP') / (metrics.get('TP') + metrics.get('FP'))
        metrics['recall'] = metrics.get('TP') / (metrics.get('TP') + metrics.get('FN'))
        metrics['f_score'] = 2 * ((metrics.get('precision') * metrics.get('recall')) / (metrics.get('precision') + metrics.get('recall')))
        #temp = metrics.get('TP') / (metrics.get('TP') + 0.5 * (metrics.get('FP') + metrics.get('FN')))
        #print(metrics.__str__())
        #print(temp)
        return metrics
    
    @staticmethod
    def write_metrics_summary(metrics_summary):
        summary_file_path = Path('summary.csv')
        summary_file_path.touch(exist_ok=True)
        with summary_file_path.open('w') as opened_file:
            csv_writer = writer(opened_file)
            #keys = [tool_harness_instance.get_harness_type() + '_' + key for key in metrics_summary.keys()]
            for tool_name in metrics_summary.keys():
                for metric in metrics_summary.get(tool_name):
                    csv_writer.writerow([tool_name + '_' + metric, metrics_summary.get(tool_name).get(metric)])

                


if __name__ == '__main__':
    GenerateMetrics.generate('snyk')