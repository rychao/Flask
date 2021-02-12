import sys
import requests
import json
#import prism_auth

def covid():
    base_url = 'https://api.covid19api.com/live/country/italy/status/confirmed'
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()

    url = base_url #add url indexes
    req = s.get(url, verify=False)
    resp = req.json()
    return resp

if __name__ == '__main__':
    result = covid()
    column = list(result.keys())
    print(column)
