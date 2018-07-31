client = '1301_21fdynrolhnosw4k0oscogw4g8scc0w0swk4sg04s0k4cowokw'
client_secret  = '5h4de4mpcocogk4g48g4o4kwcksg0wso4k8wc8g04ookcg4oow'

access_token = 'MTY2NmFjOWU2OTFiYzQxNTg0YTM2MWUyMDQ2NDdmMTgyMTEzZjI0Z'\
               'jA3OGUxNTNjMDU4MzBjZTgyNjc2ZGUyMA'


account_id = '875500_4h4agt3gm1ogwg04c0o8woww8sc0wks4s4gg0s4ogwc80c8oow'



#with urllib.request.urlopen(

account_id = ''
alert_id = '1365784'
limit = '1000'

#  Date format
#  Year-Month-Day T Hour:Minute:Seconds.Milliseconds+TimeZone
#  yyy-MM-ddTHH:mm:ss:SSSSS+HH:mm

before_date = '2018-07-07T00:00:00.12345+02:00'
not_before_date = '2018-07-01T00:00:00.12345+02:00'
source = 'web'
unread = '1'
favorite = '1'
folder = 'archive'
tone = '1'  #  can accept array '{'-1', '0', '1'}'
countries = 'SA' #  can accept array '{'SA', 'NG'}'
include_children = 1
sort = 'domain_reach'
languages = 'en'  #  can accept array '{'en', 'af'}'
timezone = 'South_Africa/Johannesburg'
q = 'micra source:(web OR twitter) in:(inbox OR archive)'
cursor = ''

api_url = 'https://api.mention.net/api/accounts/{}/alerts/{}/mentions?limit={}'\
          '&before_date={}&not_before_date={}&source={}&unread={}&favorite={}'\
          '&folder={}&tone={}&countries={}&include_children={}&sort={}'\
          '&languages={}&timezone={}&q={}&cursor={}'.format(account_id,
                                                            alert_id,
                                                           limit,
                                                           before_date,
                                                           not_before_date,
                                                           source,
                                                           unread,
                                                           favorite,
                                                           folder,
                                                           tone,
                                                           countries,
                                                           include_children,
                                                           sort,
                                                           languages,
                                                           timezone,
                                                           q,
                                                           cursor)


with requests.Session() as s:
    s.auth = OAuth2BearerToken(access_token)
    r = s.get(api_url)
    r.raise_for_status()
    data = r.json()

##data = {'Accept' : 'application/json',
##        'Accept-Language' : 'en',
##        'Authorization' : 'Bearer ' + access_token
##        }

#response = requests.get(api_url)

#print(data)

j = json.dumps(data)

with open('nissan_mentions.json', 'w') as file:
    json.dump(data, file)


'/api/accounts/875500_4h4agt3gm1ogwg04c0o8woww8sc0wks4s4gg0s4ogwc80c8oow/'\
'alerts/1365784/mentions?limit=20&before_date=2018-07-19T12%3A36%3A10.83524100%2B00%3A00'
