# Mention-Python

Python wrapper for [Mention API](https://dev.mention.com/current/) .

## Supported API
- [Fetch application data](https://dev.mention.com/current/src/app/Appdata.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)

## Installation

    pip install mention

## Examples
```python
import mention

# Parameters
access_token = YOUR_ACCESS_TOKEN

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
								 alert_id, limit,before_date, 
								 not_before_date, source,
								 unread,favorite,
								 tone,countries,
								 include_children,folder,
								 sort, languages,
								 timezone, q, cursor)
				 
results = client.query()
```