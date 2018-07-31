# Mention-Python

Python wrapper for [Mention API](https://dev.mention.com/current/) .

## Supported API
- [Fetch a mention](https://dev.mention.com/current/src/account/alert/mention/GetMention.html)
- [Fetch a mentions](https://dev.mention.com/current/src/account/alert/mention/GetMentions.html)


## Installation

    pip install mention-python

## Examples
```python
import mention

# Parameters
api_key = YOUR_API_KEY
domain = "mention.com/dev"


#================================
# MentionAPI
#================================
client = mention.MentionAPI(api_key)
results = client.query()

```