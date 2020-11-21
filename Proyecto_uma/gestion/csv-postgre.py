#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import csv,json
from os import listdir

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "nico.2012",
                                  host = "127.0.0.1",
                                  port = "56824",
                                  database = "ProyectoUma")

    cursor = connection.cursor()
    
    data=open('./uma_02.csv','r', encoding='utf-8')
    reader=csv.reader(data)
    for row in reader:
        if row[0]=="time":
            pass
        else:
            query = "INSERT INTO datos_uma (time,uma,lat,lon,mp01,mp25,mp10,d03,d05,d01,d25,d50,d10,vel) VALUES('"+row[0]+"',"+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+");"
            cursor.execute(query)
            connection.commit()
    cursor.execute("SELECT * FROM public.datos_uma;")
    record = cursor.fetchall()
    for row in record:
        print("output: ", row,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")