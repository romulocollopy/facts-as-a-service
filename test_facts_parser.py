# coding: utf-8

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins
else:
    import builtins

import unittest
from unittest import TestCase
from mock import patch, mock_open, Mock

from facts_parser import FactsParser


CONTENT = (
u"""27 de mar 17:25 - Elias Tandel: Saiu single novo do Macaco Bong.
27 de mar 17:32 - Bernardo Fontes: e disco novo do Cícero
27 de mar 17:34 - Rômulo Collopy: "Não guardo nem dinheiro, vou guardar código comentado?" #facts
27 de mar 17:34 - Flávio Amieiro: Hahahahah
27 de mar 17:35 - Bernardo Fontes: caralho excelente essa
27 de mar 17:43 - Elias Tandel: Hahahaha
27 de mar 17:34 - Bernando Fontes: "Vou pra Friburgo vacinar o gado." #facts
27 de mar 17:46 - Bernardo Fontes: <Mídia omitida>""")

FACTS = [
    u'"Não guardo nem dinheiro, vou guardar código comentado?" #facts',
    u'"Vou pra Friburgo vacinar o gado." #facts']


class TestFactParser(TestCase):
    """ Tests if whatsapp history can be read and facts are written to file"""
    def setUp(self):
        """ Mocks file and read content """
        with patch.object(builtins, 'open', mock_open(read_data=CONTENT)):
            self.parser = FactsParser('#posdojo.txt')
            self.parser.read()

    def test_read_file(self):
        """ Test mocked file content was read """
        parser = self.parser
        self.assertEqual(CONTENT, parser.file_content)

    def test_find_facts(self):
        """ Tests if facts are found """
        self.assertEqual(FACTS, self.parser.get_facts())

    def test_create_facts(self):
        """ Mock file and assert if write is called with facts """
        with patch.object(builtins, 'open', mock_open(read_data=CONTENT)):
            self.parser.write_file()
            self.parser.output_file.write.assert_called_with(FACTS)


if __name__ == '__main__':
    unittest.main()
