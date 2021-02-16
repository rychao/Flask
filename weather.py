import sys
import requests
import json

# Retrieves data in json format and prints list
def weather(apikey):
    base_url = 'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key={}'.format(apikey)
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()

    url = base_url #add url indexes
    req = s.get(url, verify=False)
    resp = req.json()
    return resp

if __name__ == '__main__':
    sys.argv[:]
    result = weather(sys.argv[1])
    print(result)

    # column = list(result.keys())
    # print(column)

# Do readme for flaskenv keys
# Put results into postgres w/ riot script
# pull into api layer w/ flask?
