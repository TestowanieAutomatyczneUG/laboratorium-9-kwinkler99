from src.SomeClass import *
from unittest.mock import *
from unittest import TestCase, main

class test_SomeClass_public_interface(TestCase):
    def test_public_method(self):
        #prepare mock
        test_object = SomeClass()
        test_object.hidden_method = Mock(name = 'hidden_method')
        test_object.hidden_method.return_value = 10

        #testing
        result = test_object.public_method(5)
        self.assertEqual(15, result, 'return value from public_method incorrect')

if __name__ == '__main__':
    main()
