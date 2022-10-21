from XmlProtocolParser import *
import unittest
import logging 
import sys
# python -m unittest -v testXmlProtocolParser


class TestXmlParser(unittest.TestCase):

    def setUp(self):
        self.xmlParser = XmlProtocolParser()
        self.commands = self.xmlParser.importCommandsFromXml()

    def test_read_time(self):
        assert self.xmlParser.getCommand("read_time").prepareRequest() == "T" # should be "T"

    def test_set_time(self):
        assert self.xmlParser.getCommand("set_time").setValue("101112082915") == "t101112082915" # 10.11.2012 08:29:15
        print(self.xmlParser.getCommand("set_time").prepareRequest())

    def test_read_analog_channels(self):
        # assert self.xmlParser.getCommand("read_temperature") == "A0" # doc: A0

        assert self.xmlParser.getCommand("read_temperature").prepareRequest() == "A0" # doc: A0
        assert self.xmlParser.getCommand("read_humidity").prepareRequest() == "A1"
        assert self.xmlParser.getCommand("read_water_storage").prepareRequest() == "A2"
        assert self.xmlParser.getCommand("read_temp_supply_air").prepareRequest() == "A3"
        assert self.xmlParser.getCommand("read_temp_exh_air").prepareRequest() == "A4"
        assert self.xmlParser.getCommand("read_humid_suppl_air").prepareRequest() == "A5"
        assert self.xmlParser.getCommand("read_humid_exh_air").prepareRequest() == "A6"
        assert self.xmlParser.getCommand("read_all_channels").prepareRequest() == "Aa"

        log = logging.getLogger("TestXmlParser.test_read_analog_channels")
        log.debug("test = %s", self.xmlParser.getCommand("read_temperature"))

    def test_set_temperature(self):
        self.xmlParser.getCommand("set_temperature").setValue("-12.5")
        assert self.xmlParser.getCommand("set_temperature").prepareRequest() == "a0 -12.5"

        self.xmlParser.getCommand("set_temperature").setValue("-75.0")
        assert self.xmlParser.getCommand("set_temperature").prepareRequest() == "a0 -75.0"

        # TODO: prepare wrong argument handling
        self.xmlParser.getCommand("set_temperature").setValue("-77.0")
        assert self.xmlParser.getCommand("set_temperature").prepareRequest() == None
      
        self.xmlParser.getCommand("set_temperature").setValue("185.00")
        assert self.xmlParser.getCommand("set_temperature").prepareRequest() == "a0 185.00"

        self.xmlParser.getCommand("set_temperature").setValue("185.10")
        assert self.xmlParser.getCommand("set_temperature").prepareRequest() == None

    def test_set_humidity(self):
        self.xmlParser.getCommand("set_humidity").setValue("-0.01")
        assert self.xmlParser.getCommand("set_humidity").prepareRequest() == None

        self.xmlParser.getCommand("set_humidity").setValue("0.01")
        assert self.xmlParser.getCommand("set_humidity").prepareRequest() == "a1 0.01"

        self.xmlParser.getCommand("set_humidity").setValue("50.00")
        assert self.xmlParser.getCommand("set_humidity").prepareRequest() == "a1 50.00"

        self.xmlParser.getCommand("set_humidity").setValue("98.00")
        assert self.xmlParser.getCommand("set_humidity").prepareRequest() == "a1 98.00"

        self.xmlParser.getCommand("set_humidity").setValue("100.00")
        assert self.xmlParser.getCommand("set_humidity").prepareRequest() == None


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("TestXmlParser.test_read_analog_channels").setLevel(logging.DEBUG)
    unittest.main()
    