import sys
import csv
import sqlite3


csv_file=sys.argv[1]
connector= sqlite3.connect(csv_file.split('.')[0]+".db")
connector.execute('CREATE TABLE databaseTable (id INT PRIMARY KEY,date TEXT, start TEXT, VisitorNeutral TEXT,PTS TEXT, HomeNeutral TEXT, PTS1 TEXT,Unnamed6 TEXT,Unnamed7 TEXT,Attend TEXT,Notes TEXT )')
with open(csv_file) as csvfile:
    csv_object = csv.DictReader(csvfile,delimiter = ',')
    for row in csv_object:
        connector.execute("INSERT INTO databaseTable (id,date,start, VisitorNeutral, PTS, HomeNeutral, PTS1, Unnamed6, Unnamed7, Attend, Notes)"+" VALUES (?,?,?,?,?,?,?,?,?,?,?)",list(row.values()))