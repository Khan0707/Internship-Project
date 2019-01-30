
from flask_restful import Resource, reqparse
from flask import request
import mysql.connector
import csv
import spacy as _s
from collections import Counter as _c
from operator import itemgetter as _ig


_nlp = _s.load('en')




# csv file name 
filename = "dummy1.csv"

###SQL
mySQLconnection= mysql.connector.connect(host='localhost',
                             database='voiceapp',
                             user='root',
                             password='Qwerty1234567#')

sql_select_Query = "select * from dummy3"
cursor = mySQLconnection .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()


keyword=['sales','revenue','apparel','discounted item','average count','popular product','location','source']
ct = 1

class QueryService(Resource):
    def post(self):
        arg1 = parser.parse_args()
        result = clf.predict(arg1["data"])
        return result


class QueryAnalyzer(object):
     

    def predict(self, data):
        file = open(filename , 'r')
        try:
    #### If sql is the  word then this shoul implement

            if "sql" in data.lower():
                for key in keyword:
                    if key  in data.lower():
                        for row in records:
                            if row[ct] == key:
                                response=row[3]
                        return response
                return "Please try again"

### If excel is the  word then this shoul implement
            elif "excel" in data.lower():
                for key in keyword:
                    if key  in data.lower():
                        for row in csv.reader(file,delimiter=','):
                            if row[ct] == key:
                                response=row[3]
                        return response
                return "Please try again"
            return "Please mention your source"
        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False

parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()
