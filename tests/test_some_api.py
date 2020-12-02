import json
from src.ExternalModule import *
from unittest.mock import *
from unittest import TestCase, main


class test_some_api(TestCase):
    @patch.object(ExternalModule,'api_call')
    def test_some_func(self, mock_api_call):
        mock_api_call.return_value = Mock(status_code = 200,
                                          response=json.dumps({'key': 'value'}))
        test_object = ExternalModule()
        result = test_object.some_func()
        self.assertEqual(result.status_code,200, "returned status code is not 200")
        self.assertEqual(result.response, '{"key": "value"}','response JSON incorrect')

if __name__ == '__main__':
    main()
