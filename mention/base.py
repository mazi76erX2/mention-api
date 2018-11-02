import requests
from requests_oauth2 import OAuth2BearerToken
from abc import ABCMeta, abstractmethod
from requests.exceptions import HTTPError
from mention import utils


class Mention(object):
    __metaclass__ = ABCMeta

    def __init__(self, access_token):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token
        """
        self.access_token = access_token

    @property
    def _base_url(self):
        return "https://api.mention.net/api"

    @abstractmethod
    def params(self):
        return

    @abstractmethod
    def url(self):
        return

    @abstractmethod
    def query(self):
        return


class AppDataAPI(Mention):
    def __init__(self, access_token):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token
        """
        self.access_token = access_token
        super(AppDataAPI, self).__init__(access_token)


    @property
    def url(self):
        end_url = "/app/data"

        return self._base_url + end_url

    
    def query(self):
        #with requests.Session() as session:
        session = requests.Session()
        session.auth = OAuth2BearerToken(self.access_token)
        response = session.get(self.url)
        try:
            response.raise_for_status()
        except HTTPError:
            pass
        session.close()
        data = response.json()

        return data


class FetchAnAlertAPI(Mention):
    def __init__(self, access_token, account_id, alert_id):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        account_id: string
            Id of the account.

        alert_id: string
            Id of the alert.
        """
        self.access_token = access_token
        self.account_id = account_id
        self.alert_id = alert_id
        super(FetchAnAlertAPI, self).__init__(access_token)


    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        params["alert_id"] = self.alert_id
        return params


    @property
    def url(self):
        end_url = ("/accounts/{account_id}/alerts/"\
            "{alert_id}".format(**self.params))

        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.get(self.url)
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data    


class CreateAnAlertAPI(Mention):
    def __init__(self,
                 access_token,
                 account_id,
                 alert_id,
                 name,
                 query,
                 languages,
                 countries,
                 sources,
                 blocked_sites,
                 noise_detection,
                 reviews_pages):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        account_id: string
            Id of the account.

        alert_id: string
            Id of the alert.

        name: string
            Alert name

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.

        alert_id: string
            Id of the alert.
        """
        self.access_token = access_token
        self.account_id = account_id
        self.alert_id = alert_id
        super(FetchAnAlertAPI, self).__init__(access_token)


    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        params["alert_id"] = self.alert_id
        return params


    @property
    def url(self):
        end_url = ("/accounts/{account_id}/alerts/"\
            "{alert_id}".format(**self.params))

        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.post(self.url, data = {'key':'value'})
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data
    


class FetchAlertsAPI(Mention):
    def __init__(self, access_token, account_id):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        account_id: string
            Id of the account.

        """
        self.access_token = access_token
        self.account_id = account_id
        super(FetchAlertsAPI, self).__init__(access_token)


    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        return params

    @property
    def url(self):
        end_url = ("/accounts/{account_id}/alerts".format(**self.params))
        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.get(self.url)
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data


class FetchAMentionAPI(Mention):
    def __init__(self, access_token, account_id, alert_id, mention_id):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        account_id: string
            Id of the account.

        alert_id: string
            Id of the alert.

        mention_id: string
            Id of the mention.
        """
        self.access_token = access_token
        self.account_id = account_id
        self.alert_id = alert_id
        self.mention_id = mention_id
        super(FetchAMentionAPI, self).__init__(access_token)


    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        params["alert_id"] = self.alert_id
        params["mention_id"] = self.mention_id
        return params


    @property
    def url(self):
        end_url = ("/accounts/{account_id}/alerts/{alert_id}/mentions/"
                   "{mention_id}".format(**self.params))

        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.get(self.url)
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data


class FetchMentionsAPI(Mention):
    def __init__(self,
                 access_token,
                 account_id,
                 alert_id,
                 since_id=None,
                 limit=None,
                 before_date=None, # 2018-07-07T00:00:00.12345+02:00
                 not_before_date=None, # #2018-07-01T00:00:00.12345+02:00
                 source=None,
                 unread=None,
                 favorite=None,
                 folder=None,
                 tone=None,
                 countries=None,
                 include_children=None,
                 sort=None,
                 languages=None,
                 timezone=None,
                 q=None,
                 cursor=None):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        alert_id: string
            Id of the alert.

        since_id: string
            Returns mentions ordered by id
            Can not be combined with before_date, not_before_date, cursor.

        limit: string
            Number of mentions to return. max 1000.

        before_date: string
            Mentions Before date in 'yyyy-MM-dd HH:mm' format
            eg. '2018-11-25 12:00'

        not_before_date: string
            Mentions Not before date in 'yyyy-MM-dd HH:mm' format
            eg. '2018-10-04 12:00'

        source: string
            Must be either web, twitter, blogs, forums, news, facebook, images or videos

        unread: boolean
            return only unread mentions.
            Must not be combined with favorite, q, and tone.

        favorite: boolean
            Whether to return only favorite mentions.
            Can not be combined with folder, when folder is not inbox or archive

        folder: string
            Filter by folder. Can be: inbox, archive, spam, trash.
            With spam and trash, include_children is enabled by default.

        tone: string
            Filter by tone. Must be one of 'negative', 'neutral', 'positive'

        countries: string
            Filter by country

        include_children: boolean
            include children mentions.

        sort: string
            Sort results. Must be one of published_at, author_influence.score,
            direct_reach, cumulative_reach, domain_reach.

        languages: string
            Filter by language

        timezone: string
            Filter by timezone

        q: string
            Filter by q

        cursor: string
            Filter by cursor
        """
        self.access_token = access_token
        self.account_id = account_id
        self.alert_id = alert_id

        self.limit = limit

        self.since_id = since_id

        if before_date is not None:
            self.before_date = utils.transform_date(before_date)
        else:
            self.before_date = before_date

        if not_before_date is not None:
            self.not_before_date = utils.transform_date(not_before_date)
        else:
            self.not_before_date = not_before_date
        
        self.source = source

        if unread is not None:
            self.unread = utils.transform_boolean(unread)
        else:
            self.unread = unread

        if favorite is not None:
            self.favorite = utils.transform_boolean(favorite)
        else:
            self.favorite = favorite
        
        self.folder = folder

        if tone is not None:
            self.tone = tone = utils.transform_tone(tone)
        else:
            self.tone = tone
 
        self.countries = countries

        if include_children is not None:
            self.include_children = utils.transform_boolean(include_children)
        else:
            self.include_children = include_children

        self.sort = sort                        
        self.languages = languages
        self.timezone = timezone
        self.q = q
        self.cursor = cursor
        super(FetchMentionsAPI, self).__init__(access_token)
        

    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        params["alert_id"] = self.alert_id

        if self.since_id:
            params["since_id"] = self.since_id
        else:
            params["before_date"] = self.before_date if self.before_date else ""
            params["not_before_date"] = self.not_before_date if self.before_date else ""
            params["cursor"] = self.cursor if self.cursor else ""

        if self.unread:
            params["unread"] = self.unread
        else:
            if (self.favorite) and
            ((self.folder == "inbox") or (self.folder == "archive")):
                params["favorite"] = self.favorite
                params["folder"] = self.folder
            else:
                 params["folder"] = self.folder if self.folder else ""   
            params["q"] = self.q if self.q else ""
            params["tone"] = self.tone if self.tone else ""

        if int(self.limit) > 1000:
            params["limit"] = "1000"
        elif int(self.limit) < 1:
            params["limit"] = ""
        else:
            params["limit"] = self.limit

        params["source"] = self.source if self.source else ""

        params["countries"] = self.countries if self.countries else ""
        params["include_children"] = self.include_children if self.include_children else ""
        params["sort"] = self.sort if self.sort else ""
        params["languages"] = self.languages if self.languages else ""
        params["timezone"] = self.timezone if self.timezone else ""
        
        

        for key, value in list(params.items()):
            if value == '':
                del params[key]
                
        return params

    @property
    def url(self):
        end_url= "/accounts/{account_id}/alerts/{alert_id}/mentions?"

        def without_keys(d, keys):
            return {x: d[x] for x in d if x not in keys}

        keys = {"access_token", "account_id", "alert_id"}
        parameters = without_keys(self.params, keys)

        for key, value in list(parameters.items()):
            if value != '':
                end_url += '&' + key + '={' + key + '}'
        
        end_url = end_url.format(**self.params)
        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.get(self.url)
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data


class FetchMentionChildrenAPI(Mention):
    """""This class will allow you to fetch a list of all children mentions for
    a given mention.
    """""
    def __init__(self, access_token, account_id, alert_id, mention_id,
                 limit=None, before_date=None):
        """
        Parameters
        ----------
        access_token: string
            Mention API access_token

        account_id: string
            Id of the account.

        alert_id: string
            Id of the alert.

        mention_id: string
            Id of the mention.

        limit: string
            Number of mentions to return. max 1000.

        before_date: string
            Mentions Before date in 'yyyy-MM-dd HH:mm' format
            eg. '2018-11-25 12:00'
        """
        self.access_token = access_token
        self.account_id = account_id
        self.alert_id = alert_id
        self.mention_id = mention_id
        self.limit = limit
        
        if before_date is not None:
            self.before_date = utils.transform_date(before_date)
        else:
            self.before_date = before_date
        super(FetchChildrenMentionAPI, self).__init__(access_token)


    @property
    def params(self):
        params = {}
        params["access_token"] = self.access_token
        params["account_id"] = self.account_id
        params["alert_id"] = self.alert_id
        params["mention_id"] = self.mention_id
        params["before_date"] = self.before_date if self.before_date else ""

        if int(self.limit) > 1000:
            params["limit"] = "1000"
        elif int(self.limit) < 1:
            params["limit"] = ""
        else:
            params["limit"] = self.limit
        
        return params


    @property
    def url(self):
        end_url= ("/accounts/{account_id}/alerts/{alert_id}/mentions/"
                  "{mention_id}/children?")

        def without_keys(d, keys):
            return {x: d[x] for x in d if x not in keys}

        keys = {"access_token", "account_id", "alert_id"}
        parameters = without_keys(self.params, keys)

        for key, value in list(parameters.items()):
            if value != '':
                end_url += '&' + key + '={' + key + '}'
        
        end_url = end_url.format(**self.params)
        return self._base_url + end_url


    def query(self):
        with requests.Session() as session:
            session.auth = OAuth2BearerToken(self.access_token)
            response = session.get(self.url)
            try:
                response.raise_for_status()
            except HTTPError:
                pass
            data = response.json()

        return data
