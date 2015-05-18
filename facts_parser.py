# coding: utf-8
import re
from datetime import datetime

class FactsParser(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            self.file_content = f.read()

    def get_facts(self):
        regex = re.compile(r': (.+#facts)', re.UNICODE)
        self.facts = regex.findall(self.file_content)

    def write_file(self):
        try:
            self.facts
        except AttributeError:
            self.get_facts()
        date = datetime.now().isoformat()
        filename = "{}_facts.txt".format(date)
        with open (filename, 'w') as self.output_file:
            self.output_file.write('\n'.join(self.facts))
