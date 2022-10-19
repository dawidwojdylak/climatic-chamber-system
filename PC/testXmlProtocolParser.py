from XmlProtocolParser import *
import unittest
import logging 
import sys
# python -m unittest -v testXmlProtocolParser

test = 0

class TestXmlParser(unittest.TestCase):


    def setUp(self):
        global test
        self.xmlParser = XmlProtocolParser()
        self.commands = self.xmlParser.importCommandsFromXml()

    def test_read_time(self):
        assert self.xmlParser.getCommand("read_time").prepareRequest() == "T" # should be "T"

    def test_set_time(self):
        self.xmlParser.getCommand("set_time").setValue("101112082915") # 10.11.2012 08:29:15
        print(self.xmlParser.getCommand("set_time").prepareRequest())
        pass

    def test_read_analog_channels(self):
        assert self.xmlParser.getCommand("read_temperature").prepareRequest() == "A0" # doc: A0
        assert self.xmlParser.getCommand("read_temperature") == "A0" # doc: A0

        log = logging.getLogger("TestXmlParser.test_read_analog_channels")
        log.debug("test = %s", self.xmlParser.getCommand("read_temperature"))

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("TestXmlParser.test_read_analog_channels").setLevel(logging.DEBUG)
    unittest.main()
    