import sys
import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/losangeles')
def weather():
    base_url = 'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key=<REDACTED>'#.format(apikey)
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()

    url = base_url #add url indexes
    req = s.get(url, verify=False)
    resp = req.json()
    return resp

if __name__ == '__main__':
    # sys.argv[:]
    # app.config['apikey'] = sys.argv[1] pass into sysargv?
    app.run()

# Do readme for flaskenv keys
# Put results into postgres w/ riot script
# pull into api layer w/ flask?
