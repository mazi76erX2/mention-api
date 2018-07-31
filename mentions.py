import requests
import urllib.request
from requests_oauth2 import OAuth2BearerToken
import json
from abc import ABCMeta, abstractmethod


class Mention(object):
    __metaclass__ = ABCMeta

    def __init__(self, api_key):
        """
        Parameters
        ----------
        api_key: string
            Mention API key
        """
        self.api_key = api_key

    @property
    def _base_url(self):
        return "https://api.mention.net/api/accounts/"

    @abstractmethod
    def params(self):
        return

    @abstractmethod
    def url(self):
        return

    @abstractmethod
    def query(self):
        return

class FetchMentionsAPI(Mention):

    def __init__(self, api_key, domain, start_month, end_month,
                 time_granularity="MONTHLY", main_domain_only=False):
        """
        Parameters
        ----------
        api_key: string
            Mention API key
        domain: string
            Domain to query.
        start_month: string
            Start Month in (M-YYYY) format
        end_month: string
            End Month in (M-YYYY) format
        time_granularity: string
            Time granularity of report. Can be: Daily, Weekly, Monthly
        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)
        """

        self.domain = utils.domain_from_url(domain)
        
        self.alert_id = alert_id
        self.limit = limit
        self.before_date = before_date
        self.not_before_date = not_before_date
        self.source = source
        self.unread = unread
        self.favorite = favorite
        self.folder = folder
        self.tone = tone
        self.countries = countries
        self.include_children = include_children
        self.folder = folder
        self.sort = sort
        self.languages = languages
        self.timezone = timezone
        self.q = q
        self.cursor = cursor
        

        

        
        super(TrafficAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["time_granularity"] = self.time_granularity
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/visits?gr={time_granularity}&start={start_month}"
                   "&end={end_month}&md={main_domain_only}&Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Values' not in results:
            raise InvalidResponseException(results)

return results['Values']


