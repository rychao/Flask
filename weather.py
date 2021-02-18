import psycopg2
import sys
import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)

def db():
    return psycopg2.connect(user="admin", password=<REDACTED>, host=<REDACTED>, port="5432", database="my-postgres")

@app.route('/')
def query_db():
    one=False
    cur = db().cursor()
    cur.execute("select * from los_angeles_weather limit %s", (1,))
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    my_query = (r[0] if r else None) if one else r
    return json.dumps(my_query)

if __name__ == '__main__':
    # sys.argv[:]
    # app.config['apikey'] = sys.argv[1] pass into sysargv?
    # query_db("select * from los_angeles_weather limit %s", (1,), False)
    app.run()

# Do readme for flaskenv keys
# Put results into postgres w/ riot script
# pull into api layer w/ flask?
