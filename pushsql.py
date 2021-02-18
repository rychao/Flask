import sys
import json
import psycopg2
import requests

def get_weather(api_key, connection):
    url = 'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key={}'.format(api_key)
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()
    req = s.get(url, verify=False)
    resp = req.json()

    #Psycopg2 connection
    connection = connection
    cursor = connection.cursor()

    return resp

def tablemaker(city, connection, jsonresponse):

    # pollutionColumn = list(resp['data']['current']['pollution'].keys())
    weatherColumn = list(jsonresponse['data']['current']['weather'].keys())

    tableName = city + '_weather'
    #create empty dictionaries for column entries ~> '{} TEXT NOT NULL, {} TEXT NOT NULL, ...'
    column_args = ','.join([' {}    TEXT   NOT NULL'] * len(weatherColumn))

    #create sql query ~> CREATE TABLE IF NOT EXISTS summoner_by_name ( {} TEXT NOT NULL, ...)
    table = "CREATE TABLE IF NOT EXISTS {} ({})".format(tableName, column_args)

    #add columns entries ~> CREATE TABLE IF NOT EXISTS summoner_by_name ( participantId TEXT NOT NULL, ...)
    create_table = table.format(*weatherColumn)

    #create table
    connection = connection
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    #strip keys -> [6, False, 1054 ...]
    weatherRow = list(jsonresponse['data']['current']['weather'].values())

    #create empty dictionaries for row entries -->' '{}', '{}', '{}', ...'
    row_args = ','.join([' \'{}\''] * len(weatherRow))

    #create sql query ~> INSERT INTO pg_summoner_stats_match_by_id VALUES ( {} {} {} {} ...)
    entry = "INSERT INTO {} VALUES ({})".format(tableName, row_args)

    #add row entries ~> INSERT INTO summoner_by_name VALUES ( 6, False, 1054 ...)
    query_entry = entry.format(*weatherRow)

    #insert record
    cursor.execute(query_entry)
    connection.commit()
    print("Records inserted successfully")

    #fetch result
    cursor.execute("SELECT * from {}".format(tableName))
    record = cursor.fetchall()
    print("Result ", record)

def main():
    connection = psycopg2.connect( user="admin", password=<REDACTED>, host=<REDACTED>, port="5432", database="my-postgres")
    resp = get_weather(sys.argv[1], connection)
    # tablemaker(pollution, sys.argv[2], connection)
    tablemaker(sys.argv[2], connection, resp)

if __name__ == "__main__":
	sys.argv[:]
	main()
