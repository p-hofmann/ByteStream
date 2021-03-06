from io import BytesIO
from unittest import TestCase
from binarystream import BinaryStream


__author__ = 'Peter Hofmann'


class DefaultSetup(TestCase):
    """
    @type object: BinaryStream
    """

    def __init__(self, methodName='runTest'):
        super(DefaultSetup, self).__init__(methodName)
        self.object = None

    def setUp(self):
        self.object = BinaryStream(BytesIO())

    def tearDown(self):
        self.object = None


class TestBinaryStream(DefaultSetup):
    # def test_write(self):
    #     expected_result
    #     self.fail()
    
    def test_write_bool(self):
        expected_result = True
        self.object.write_bool(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_bool())
    
    def test_write_byte(self):
        expected_result = 111
        self.object.write_byte(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_byte())
    
    def test_write_int16(self):
        expected_result = 16384
        self.object.write_int16(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int16())
    
    def test_write_int16_unassigned(self):
        expected_result = 16384
        self.object.write_int16_unassigned(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int16_unassigned())
    
    def test_write_int32(self):
        expected_result = 536870912
        self.object.write_int32(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int32())
    
    def test_write_int32_unassigned(self):
        expected_result = 536870912
        self.object.write_int32_unassigned(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int32_unassigned())
    
    def test_write_int64(self):
        expected_result = 24294198314
        self.object.write_int64(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int64())
    
    def test_write_int64_unassigned(self):
        expected_result = 24294198314
        self.object.write_int64_unassigned(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_int64_unassigned())
    
    def test_write_float(self):
        expected_result = 123123.1
        self.object.write_float(expected_result)
        self.object.seek(0)
        self.assertAlmostEqual(expected_result, self.object.read_float(), 2)
    
    def test_write_double(self):
        expected_result = 9123123123.1
        self.object.write_double(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_double())
    
    def test_write_string(self):
        expected_result = "Some text"
        self.object.write_string(expected_result)
        self.object.seek(0)
        self.assertEqual(expected_result, self.object.read_string())
    
    def test_write_byte_array(self):
        expected_result = [1, 2, 3, 4, 5]
        self.object.write_byte_array(expected_result)
        self.object.seek(0)
        self.assertListEqual(expected_result, self.object.read_byte_array())
