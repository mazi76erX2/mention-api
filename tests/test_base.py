import unittest
import mock
import json
import mention


class TestAppDataAPI(unittest.TestCase):
    
    def setUp(self):
        self.access_token = "a"

        self.client = mention.AppDataAPI(self.access_token)


    def test_url(self):
        result = self.client.url
        expected = "https://api.mention.net/api/accounts/a"

        self.assertEquals(result, expected)


    @mock.patch("mention.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)


        # assert successful response
        json_payload = {
            "Values": [{
                "Date": "2013-09-01",
                "Value": 356963532.0
            }, {
                "Date": "2013-09-02",
                "Value": 370288318.0
            }, {
                "Date": "2013-09-03",
                "Value": 384481631.0
            }]
        }

        expected = [{
            "Date": "2013-09-01",
            "Value": 356963532.0
        }, {
            "Date": "2013-09-02",
            "Value": 370288318.0
        }, {
            "Date": "2013-09-03",
            "Value": 384481631.0
        }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)
