from src.car import Car
from unittest.mock import *
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.temp = Car()

    def test_needsFuel_no(self):
        # prepare mock
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = "No :D"

        # testing
        self.assertEqual(self.temp.needsFuel(), "No :D")

    def test_needsFuel_yes(self):
        # prepare mock
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = "Yes!!!"

        # testing
        self.assertEqual(self.temp.needsFuel(), "Yes!!!")

    def test_getEngineTemperature(self):
        # prepare mock
        self.temp.getEngineTemperature = Mock(name='getEngineTemperature')
        self.temp.getEngineTemperature.return_value = 200

        # testing
        self.assertEqual(self.temp.getEngineTemperature(), 200)

    @patch.object(Car, 'driveTo')
    def test_driveTo(self, mock_car):
        mock_car.return_value = "Warszawa, Polska"
        result = self.temp.driveTo("Warszawa, Polska")
        self.assertEqual(result, "Warszawa, Polska")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
