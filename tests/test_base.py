import unittest
from unittest import mock
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


    @mock.patch("mention.requests.get")
    def test_query(self, mock_requests_get):
        # assert client error response
        unsuccessful_response = {
            'error': 'invalid_grant',
            'error_description': 'The access token provided is invalid.'
        }

        expected = unsuccessful_response
        response = type('response', (object,),
                        {'text': json.dumps(unsuccessful_response)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEqual(results, expected)

        # assert successful response
        successful_response = {
            "app_languages": {"a"},
            "alert_languages": {"a"},
            "alert_countries": {"a"},
            "alert_tones": {"a"},
            "alert_sources": {"a"},
            "alert_share_roles": {"a"},
            "alert_colors": ["a"],
            "countries": {"a"},
            "task_types": {"a"},
            "mention_folders": {"a"},
            "mention_log_types": {"a"},
            "social_account_types": {"a"},
            "locale": "en",
            "week_days": {"a"},
            "push_notification_frequencies": {"a"},
            "desktop_notification_frequencies": {"a"},
            "email_notification_frequencies": {"a"},
            "trending_email_notification_frequencies": {"a"},
            "trending_sms_notification_frequencies:": {"a"}
        }

        expected = successful_response
        response = type('response', (object,),
                        {'text': json.dumps(successful_response)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()
