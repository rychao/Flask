import psycopg2
import sys
import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)

def db():
    return psycopg2.connect(user="admin", password=<REDACTED>, host=<REDACTED>, port="5432", database="my-postgres")

@app.route('/losangeles')
def la():
    one=False
    cur = db().cursor()
    cur.execute("select * from los_angeles_weather limit %s", (1,))
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    my_query = (r[0] if r else None) if one else r
    return json.dumps(my_query)

@app.route('/sanfrancisco')
def sf():
    one=False
    cur = db().cursor()
    cur.execute("select * from san_francisco_weather limit %s", (1,)) #string format city name?
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    my_query = (r[0] if r else None) if one else r
    return json.dumps(my_query)

if __name__ == '__main__':
    app.run()

# app.config['apikey'] = sys.argv[1] pass into sysargv?
# query_db("select * from los_angeles_weather limit %s", (1,), False)

# Do readme for flaskenv keys
# Put results into postgres w/ riot script
# pull into api layer w/ flask?
