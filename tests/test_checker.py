from src.checker import Checker
from unittest.mock import *
from unittest import TestCase, main


class TestChecker(TestCase):

    def setUp(self):
        self.temp = Checker()

    def test_after_17(self):
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.wavWasPlayed = Mock(name='wavWasPlayed')
        self.temp.env.getTime.return_value = 24
        self.temp.env.wavWasPlayed.return_value = True

        self.assertEqual(self.temp.reminder('Freaks like us'), True)

    def test_before_17(self):
        self.temp.env.getTime = Mock(name='getTime')
        self.temp.env.resetWav = Mock(name='resetWav')
        self.temp.env.getTime.return_value = 10
        self.temp.env.resetWav.return_value = False

        self.assertEqual(self.temp.reminder('Sociopath'), False)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
