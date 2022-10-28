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

    def test_set_temperature_gradient_up(self):
        # TODO check the units
        # check upper limit
        self.xmlParser.getCommand("set_temperature_gradient_up").setValue("-01.00")
        assert self.xmlParser.getCommand("set_temperature_gradient_up").prepareRequest() == None # min value = 00.00

        self.xmlParser.getCommand("set_temperature_gradient_up").setValue("0.00")
        assert self.xmlParser.getCommand("set_temperature_gradient_up").prepareRequest() == "u1 0.00"
        
        self.xmlParser.getCommand("set_temperature_gradient_up").setValue("59.29")
        assert self.xmlParser.getCommand("set_temperature_gradient_up").prepareRequest() == "u1 59.29"

        self.xmlParser.getCommand("set_temperature_gradient_up").setValue("999.99")
        assert self.xmlParser.getCommand("set_temperature_gradient_up").prepareRequest() == "u1 999.99"

        self.xmlParser.getCommand("set_temperature_gradient_up").setValue("1000")
        assert self.xmlParser.getCommand("set_temperature_gradient_up").prepareRequest() == None # max value = 999.9

        
    def test_set_temperature_gradient_down(self):
        self.xmlParser.getCommand("set_temperature_gradient_down").setValue("-01.00")
        assert self.xmlParser.getCommand("set_temperature_gradient_down").prepareRequest() == None # min value = 00.00

        self.xmlParser.getCommand("set_temperature_gradient_down").setValue("0.00")
        assert self.xmlParser.getCommand("set_temperature_gradient_down").prepareRequest() == "d1 0.00"
        
        self.xmlParser.getCommand("set_temperature_gradient_down").setValue("61.29")
        assert self.xmlParser.getCommand("set_temperature_gradient_down").prepareRequest() == "d1 61.29"

        self.xmlParser.getCommand("set_temperature_gradient_down").setValue("999.99")
        assert self.xmlParser.getCommand("set_temperature_gradient_down").prepareRequest() == "d1 999.99"

        self.xmlParser.getCommand("set_temperature_gradient_down").setValue("1000")
        assert self.xmlParser.getCommand("set_temperature_gradient_down").prepareRequest() == None # max value = 999.9

    def test_set_humidity_gradient_up(self):
        self.xmlParser.getCommand("set_humidity_gradient_up").setValue("-01.00")
        assert self.xmlParser.getCommand("set_humidity_gradient_up").prepareRequest() == None # min value = 00.00

        self.xmlParser.getCommand("set_humidity_gradient_up").setValue("0.00")
        assert self.xmlParser.getCommand("set_humidity_gradient_up").prepareRequest() == "u2 0.00"
        
        self.xmlParser.getCommand("set_humidity_gradient_up").setValue("59.29")
        assert self.xmlParser.getCommand("set_humidity_gradient_up").prepareRequest() == "u2 59.29"

        self.xmlParser.getCommand("set_humidity_gradient_up").setValue("999.99")
        assert self.xmlParser.getCommand("set_humidity_gradient_up").prepareRequest() == "u2 999.99"

        self.xmlParser.getCommand("set_humidity_gradient_up").setValue("1000")
        assert self.xmlParser.getCommand("set_humidity_gradient_up").prepareRequest() == None # max value = 999.9   

    def test_set_humidity_gradient_down(self):
        self.xmlParser.getCommand("set_humidity_gradient_down").setValue("-01.00")
        assert self.xmlParser.getCommand("set_humidity_gradient_down").prepareRequest() == None # min value = 00.00

        self.xmlParser.getCommand("set_humidity_gradient_down").setValue("0.00")
        assert self.xmlParser.getCommand("set_humidity_gradient_down").prepareRequest() == "d2 0.00"
        
        self.xmlParser.getCommand("set_humidity_gradient_down").setValue("59.29")
        assert self.xmlParser.getCommand("set_humidity_gradient_down").prepareRequest() == "d2 59.29"

        self.xmlParser.getCommand("set_humidity_gradient_down").setValue("999.99")
        assert self.xmlParser.getCommand("set_humidity_gradient_down").prepareRequest() == "d2 999.99"

        self.xmlParser.getCommand("set_humidity_gradient_down").setValue("1000")
        assert self.xmlParser.getCommand("set_humidity_gradient_down").prepareRequest() == None # max value = 999.9  

    def test_read_temperature_gradient(self):
        assert self.xmlParser.getCommand("read_temperature_gradient").prepareRequest() == "U1"

    def test_read_humidity_gradient(self):
        assert self.xmlParser.getCommand("read_humidity_gradient").prepareRequest() == "U2"

    def test_read_adjusted_final_value_of_the_temperature_ramp(self):
        assert self.xmlParser.getCommand("read_adjusted_final_value_of_the_temperature_ramp") == "E1"

    def test_read_adjusted_final_value_of_the_humidity_ramp(self):
        assert self.xmlParser.getCommand("read_adjusted_final_value_of_the_humidity_ramp") == "E2"

    def test_read_temperature_ramp_parameters(self):
        assert self.xmlParser.getCommand("read_temperature_ramp_parameters") == "R0"

    def test_read_humidity_ramp_parameters(self):
        assert self.xmlParser.getCommand("read_humidity_ramp_parameters") == "R1"

    def test_read_chamber_state(self):
        assert self.xmlParser.getCommand("read_chamber_state") == "S"

    def test_switch_on_chamber(self):
        assert self.xmlParser.getCommand("switch_on_chamber") == "s1 1"

    def test_switch_off_chamber(self):
        assert self.xmlParser.getCommand("switch_off_chamber") == "s1 0"

    def test_pause_chamber(self):
        assert self.xmlParser.getCommand("pause_chamber") == "s3 0"

    def test_continue_chamber(self):
        assert self.xmlParser.getCommand("continue_chamber") == "s3 1"

    def test_read_additional_digital_channels(self):
        assert self.xmlParser.getCommand("read_additional_digital_channels") == "O" # Docs 4.9.3

    def test_read_program_state(self):
        assert self.xmlParser.getCommand("read_program_state") == "P"

    def test_read_error_text(self):
        assert self.xmlParser.getCommand("read_error_text") == "F" # chamber returns error text

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("TestXmlParser.test_read_analog_channels").setLevel(logging.DEBUG)
    unittest.main()
    