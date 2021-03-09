import sys
import csv
import sqlite3

def create_DB(connector,fieldnames):
    columns=""
    for i in range(len(fieldnames)):
        columns+=("{} TEXT".format(fieldnames[i].replace(" ","_")))
        if i<(len(fieldnames)-1):
            columns+=", "
    query=('CREATE TABLE DATABASETABLE ({});'.format(columns))
    print(query)
    connector.execute(query)

def insert_into_db(connector,row):
    fieldnames=list(row.keys())
    columns=""
    for i in range(len(fieldnames)):
        columns+=(fieldnames[i].replace(" ","_"))
        if i<(len(fieldnames)-1):
            columns+=", "

    values=list(row.values())
    valuesquery=""
    for i in range(len(values)):
        valuesquery+=("'{}'".format(values[i]))
        if i<(len(values)-1):
            valuesquery+=", "

    query= "INSERT INTO DATABASETABLE ({})".format(columns)+" VALUES ({})".format(valuesquery)
    connector.execute(query)

def printdb(connector):
    cursor = connector.execute("SELECT * from DATABASETABLE")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



if __name__== "__main__":
    csv_file=sys.argv[1]
    connector = sqlite3.connect(csv_file.split('.')[0]+".db")
    with open(csv_file) as csvfile:
        csv_object = csv.DictReader(csvfile,delimiter = ',')
        create_DB(connector,csv_object.fieldnames)
        for row in csv_object:
           insert_into_db(connector,row)
    printdb(connector)
    connector.close()