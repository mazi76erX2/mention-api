import unittest
import utils


class TestTransformDate(unittest.TestCase):

    result = utils.transform_date('2018-11-25 12:00')

    def test_date(self):
        self.assertEqual(result, '2018-11-25T12%3A00%3A00.12345%2B00%3A00')


class TestTransformBoolean(unittest.TestCase):

    resultTrue = utils.transform_boolean(True)
    resultFalse = utils.transform_boolean(False)

    
    def test_true(self):
        self.assertEqual(resultTrue, '1')


    def test_false(self):
        self.assertEqual(resultFalse, '0')


class TestTransformTone(unittest.TestCase):

    resultNegative = utils.transform_tone('negative')
    resultNeutral = utils.transform_tone('neutral')
    resultPositive = utils.transform_tone('true')

    
    def test_negative(self):
        self.assertEqual(resultNegative, '-1')


    def test_neutral(self):
        self.assertEqual(resultNeutral, '0')


    def test_positive(self):
        self.assertEqual(resultPositive, '1')
