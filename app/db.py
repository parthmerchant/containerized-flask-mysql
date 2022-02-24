from app import app
import mysql.connector
import os
from flask import jsonify
from config import conf

def exec_db_query_all(query: str): 
    try:
        cnx = mysql.connector.connect(**conf)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        cnx.close()

def exec_db_query_one(query: str):
    try:
        cnx = mysql.connector.connect(**conf)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        rows = cursor.fetchone()
        return rows
    except Exception as e:
        print(e)
    finally:

