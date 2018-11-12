import sqlite3
import json
from datetime import datetime

#sql_transaction = []

connection = sqlite3.connect('{}.db')
c = connection.cursor()

timeframe = '2015-05'
sql_transaction = []

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply(title, year)""")

if __name__ == "__main__":
    create_table()
    row_counter = 0
    #paired_rows = 0
    with open("/Lyrics_LilPeep.json".format(timeframe.split(',')))
