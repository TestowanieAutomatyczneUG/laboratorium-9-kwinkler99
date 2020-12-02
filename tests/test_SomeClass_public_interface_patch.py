from src.SomeClass import *
from unittest.mock import *
from unittest import TestCase, main

class test_SomeClass_public_interface_patch(TestCase):
    @patch.object(SomeClass, 'hidden_method')
    def test_public_method(self, mock_method):
        #prepare mock
        mock_method.return_value = 10
        #testing
        test_object = SomeClass()
        result = test_object.public_method(5)
        self.assertEqual(15, result, 'return value from public_method incorrect')

if __name__ == '__main__':
    main()
