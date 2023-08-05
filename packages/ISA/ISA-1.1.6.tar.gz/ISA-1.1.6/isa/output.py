import csv
import logging

import datetime

import os
import threading
import pprint

_logger = logging.getLogger(__name__)


class OutputHandler:
    """
    Class for handling the output.
    """

    def __init__(self, output_path):
        """
        Initialize the output handler.

        :param output_path: path for storing the results (should end in .csv)
        """
        self.lock = threading.RLock()
        self.output_path = output_path
        self.output_type = 'standard_output'
        if self.output_path is not None:
            if self.output_path.lower().endswith('.csv'):
                self.output_type = 'csv'
        if self.output_path is not None and os.path.exists(self.output_path):
            raise Exception('Output file (%s) does already exist' % self.output_path)
        _logger.debug('output_type=%s' % self.output_type)
        if self.output_type == 'standard_output':
            self.printer = pprint.PrettyPrinter(indent=4)

    def process(self, node, statistics):
        """
        Result handler for a monitor.

        :param node: node as specified by the result_handler argument of Monitor
        :param statistics: statistics as specified by the result_handler argument of Monitor
        """
        if type(statistics) is not list:
            statistics = [statistics]
        for item in statistics:
            item['node'] = node
            item['time'] = datetime.datetime.now()
        if self.output_path is not None:
            if self.output_type == 'csv':
                self.output_csv(node, statistics)
        if self.output_type == 'standard_output':
            # Just print to standard output
            print('-' * 80)
            print("OutputHandler(standard_output) %s:" % datetime.datetime.now())
            print('-' * 80)
            self.printer.pprint(statistics)

    def output_csv(self, node, results):
        """
        Output a node and its result to the given CSV file.

        :param node: node as specified by the process method.
        :param results: results as specified by the process method
        """
        with self.lock:
            for result in results:
                keys = sorted(result.keys())
                exists = os.path.exists(self.output_path)
                with open(self.output_path, 'a') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=keys)
                    if not exists:
                        writer.writeheader()
                    writer.writerow(result)
