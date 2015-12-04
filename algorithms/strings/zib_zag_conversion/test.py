import unittest
from zig_zag_conversion import zig_zag_conversion


class ZigZagConversionTest(unittest.TestCase):

    def test_1_row(self):
        str_ = 'PAYPALISHIRINGIN'
        str_converted = zig_zag_conversion(str_, 1)
        self.assertEqual(str_converted, 'PAYPALISHIRINGIN')

    def test_2_row(self):
        str_ = 'COMPUTERS'
        str_converted = zig_zag_conversion(str_, 2)
        self.assertEqual(str_converted, 'CMUESOPTR')

    def test_3_rows(self):
        str_ = 'PAYPALISHIRINGIN'
        str_converted = zig_zag_conversion(str_, 3)
        self.assertEqual(str_converted, 'PAHNAPLSIIGNYIRI')

    def test_4_rows(self):
        str_ = 'NEWENGLANDPATRIOTS'
        str_converted = zig_zag_conversion(str_, 4)
        self.assertEqual(str_converted, 'NLTEGAARSWNNPITEDO')