
from flask_restful import Resource, reqparse
from flask import request
import csv




# csv file name 
filename = "dummy1.csv"
keyword=['sales','revenue','apparel','discounted item','average count','popular product','location']
ct = 1

class QueryService(Resource):
    def post(self):
        arg1 = parser.parse_args()
        result = clf.predict(arg1["data"])
        return result


class QueryAnalyzer(object):
     

    def predict(self, data):

        ###EXCEL: 1

        file = open(filename , 'r')
        try:
            for key in keyword:
                if key  in data.lower():
                    for row in csv.reader(file,delimiter=','):
                        if row[ct] == key:
                            response=row[3]
                    return response
            return "Please try again"
        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False

parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()
