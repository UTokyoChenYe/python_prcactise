from city_fullname import get_city_fullname
import unittest

class CityFullnameFunctionTestCase(unittest.TestCase):
    def test_city_fullname(self):
        get_name = get_city_fullname('Santiago', 'Chile')
        self.assertEqual(get_name, 'Santiago Chile')

unittest.main()