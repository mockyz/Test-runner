# encoding: utf-8

class TCReporter:

    def __init__(self):
        self.test_result = list()

    def add_test_result(self, test_result):
        pass

    def generate_test_result(self):
        pass


class PlainReporter(TCReporter):

    def __init__(self):
        self.report_logs = dict()

    def log_step(self, case_id, line):
        if self.report_logs.get(case_id) is None:
            self.report_logs[case_id] = [line]
        print(line)

    def complete_report(self):
        pass

    def flush_file(self):
        pass

    def generate_report(self):
        pass
