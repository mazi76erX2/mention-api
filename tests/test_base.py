import unittest
from unittest.mock import Mock, patch
from exceptions import InvalidResponseException
import json
import mention

class TestAppDataAPI(unittest.TestCase):
    
    def setUp(self):
        self.access_token = "a"
        
        self.client = mention.AppDataAPI(self.access_token)


    def test_url(self):
        result = self.client.url
        expected = "https://api.mention.net/api/app/data"

        self.assertEqual(result, expected)


    @patch("mention.requests.get")
    def test_query_error(self, mock_requests_get):
        # assert client error response
        unsuccessful_response = {
            'error': 'invalid_grant',
            'error_description': 'The access token provided is invalid.'
        }
        
        response = type('response', (object,),
                        {'text': json.dumps(unsuccessful_response)})
        
        mock_requests_get.return_value = response
        self.assertEqual(unsuccessful_response, self.client.query())

    
    @patch("mention.requests.get")
    def test_query_success(self, mock_requests_get):
        # assert successful response
        with open("testapidata.json", "r") as read_file:
            successful_response = json.load(read_file)

        with open("api_keys.json", "r") as read_file:
            self.access_token = json.load(read_file)["access_token"]
            self.client = mention.AppDataAPI(self.access_token)

        mock_requests_get.return_value = Mock(ok=True)
        mock_requests_get.return_value.json.return_value = successful_response

        response = type('response', (object,),
                        {'text': json.dumps(successful_response)})

        self.assertEqual(successful_response, self.client.query())


if __name__ == '__main__':
    unittest.main()
