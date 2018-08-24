# Mention-Python

Python wrapper for [Mention API](https://dev.mention.com/current/) .

## Supported API
- [Fetch application data](https://dev.mention.com/current/src/app/Appdata.html)
- [Fetch an alert](https://dev.mention.com/current/src/account/alert/GetAlert.html)
- [Fetch all alert of an account](https://dev.mention.com/current/src/account/alert/GetAlerts.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch mentions](https://dev.mention.com/current/src/account/alert/mention/GetMentions.html)

## Installation

    pip install setup.py

## Examples
```python
import mention

# Parameters
access_token = YOUR_ACCESS_TOKEN
account_id = YOUR_ACCOUNT_ID

alert_id =  YOUR_ALERT_ID
mention_id = YOUR_MENTION_ID

limit = "20"
before_date = "2018-07-07" # in format YYY-MM-DD
not_before_date = "2018-07-01" # in format YYY-MM-DD
source = "web"
unread = False
favorite = False
folder = "inbox"
tone = "neutral"
countries = "ZA"
include_children = False
sort = "domain_reach"
languages = "en"
timezone = "SouthAfrica/Johannesburg"
q = "nasa source:(facebook OR twitter) in:(inbox OR archive)"

#================================
# AppDataAPI
#================================
client = mention.AppDataAPI(access_token)
results = client.query()

#================================
# FetchAnAlertAPI
#================================
client = mention.FetchAnAlertAPI(access_token, account_id,
                                    			alert_id)
results = client.query()

#================================
# FetchAlertsAPI
#================================
client = mention.FetchAnAlertAPI(access_token, account_id)
results = client.query()

#================================
# FetchAMentionAPI
#================================
client = mention.RankAndReachAPI(access_token, account_id,
                                    alert_id, mention_id)
results = client.query()

#================================
# FetchAllMentionsAPI
#================================
client = mention.RankAndReachAPI(access_token, account_id,
								 alert_id, limit, before_date,
								 not_before_date, source,
								 unread,favorite,
								 tone,countries,
								 include_children,folder,
								 sort, languages,
								 timezone, q, cursor)
				 
results = client.query()
```