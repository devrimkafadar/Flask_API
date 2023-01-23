from flask import Flask, request, url_for, redirect
from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import json

load_dotenv()
db = Flask(__name__)
url = os.getenv("DATABASE_URL")

def onlyQueryDBoperation(query):
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except:
            print('NOOOOO')

        connection.commit()
    except:
        psycopg2.DatabaseError
    finally:
        cursor.close()
        connection.close()



def getRequestedDataFromDB(query):
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except:
            print('NOOOO')
        list_to_return = cursor.fetchall()
        return list_to_return
    except:
        psycopg2.DatabaseError
    finally:
        cursor.close()
        connection.close()
        
        
def manipulateDBWithGivenData(postQuery, val):
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        print(val)
        print(type(val))
        try:
            cursor.execute(postQuery,val)
        except:
            print("nooo")
        connection.commit()
        print('try')
    except:
        psycopg2.DatabaseError
    finally:
        cursor.close()
        connection.close()
        
def manipulateDBWithGivenData2(postQuery, val):
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        try:
            cursor.execute(postQuery)
        except:
            print('NOOOO')
        list_to_return = cursor.fetchall()
        connection.commit()
        return list_to_return
    except:
        psycopg2.DatabaseError
    finally:
        cursor.close()
        connection.close()

def addGivenData(postQuery, val):
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        try:
            cursor.execute(postQuery,val)
        except:
            print("NOOOO")
        connection.commit()
        print('try')
    except:
        psycopg2.DatabaseError
    finally:
        cursor.close()
        connection.close()
