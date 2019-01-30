
from flask_restful import Resource, reqparse
from flask import request
import csv
import pandas as pd 
import re
import numpy as np
from nltk.corpus import stopwords      ###removing stopwords
from difflib import get_close_matches  ### close matches
from itertools import chain            ###list flatening

#closeMatches(concepts, word)

concepts= ["baby shop","babyshop","candelite","emax","fitness first","foodmark","funcity","home box","home centre","other hospitality", "division","iconic","koton",
"lifestyle","lipsy","max","new look","reiss","sarah","shoexpress","splash","sports one","yours london","icare clinics","centrepoint","shoe mart",
"hospitality division","lrl total"]



metrics=['srp' ,'srp percentage change','members' ,'members percentage change','ams','ams percentage change','atv','atv percentage change','upt' ,
'upt percentage change', 'new percentage','new percentage change','existing percentage','existing percentage change','churn percentage','churn percentage change',
'repeat customer percentage','repeat customer percentage change','repeat revenue percentage','repeat revenue percentage change','gold customer','gold customer percentage change',
'gold revenue percentage','gold revenue percentage change', 'vintage customer','vintage customer percentage change','vintage revenue','vintage revenue percentage change','store percentage',
'store customer percentage change',' store revenue',' store revenue percentage change','online percentage','online customer percentage change', 
'online revenue ','online revenue percentage change','omnichannel customer','omnichannel customer percentage change','omni channel customer','omni channel customer percentage change',
'omnichannel revenue','omnichannel revenue percentage change', 'omni channel revenue','omni channel revenue percentage change','valid mobile customer', 'valid mobile customer percentage change',
'valid email customer','valid email customer percentage change','mobile app customer','mobile app customer percentage change','shukran active customer',
'shukran active customer percentage change', 'enrollment','enrollment percentage change','high value customer','high value customer percentage change','high value revenue', 
'high value revenue percentage change','sukran active customer','sukran active customer percentage change']

#ct = 0
#cs = 2
#col_num = list(range(2,55))
class QueryService(Resource):
    def post(self):
        arg1 = parser.parse_args()
        result = clf.predict(arg1["data"])
        return result


class QueryAnalyzer(object):

    def closeMatches(patterns, word): 
     return(get_close_matches(word, patterns)) 
     

    def predict(self, data):
        file = pd.read_csv("lmgg.csv")
        file=file.set_index('Concept')
        file.columns = file.columns.str.lower()
        file.columns = file.columns.str.rstrip()
        file.index = file.index.str.lower()
        file.columns= file.columns.map(lambda x:re.sub('\s+',' ',x).strip())
        try:
            for concept in concepts:
                for metric in metrics:
                    if concept in data.lower() and metric in data.lower():

                        if re.search("change",data) is None:
                            resp1= file.loc[concept,metric]
                            if (resp1>0 and resp1<1):
                                resp1= resp1 * 100
                                resp1=(np.rint(resp1))  
                            else:
                                resp1=(np.rint(resp1))
                                  
                            if re.search("percentage",metric) is None:
                                resp2 = file.loc[concept,metric+" percentage change"]
                            else:
                                resp2 = file.loc[concept,metric+" change"]
                            
                            if (resp2<0 and resp2>-1):  ### CASE OF negatives     
                                resp2= resp2 * 100
                                resp2=(np.rint(resp2))
                                return("The {} for {} is {} and it has decreased by {} percent since last year.".format(metric.title(),concept.title(),resp1, abs(resp2)))
                            elif(resp2 < -1):
                                resp2=(np.rint(resp2))
                                return("The {} for {} is {} and it has decreased by {} percent since last year.".format(metric.title(),concept.title(),resp1, abs(resp2)))
                ##### bwetween 0 and 1
                            elif (resp2>0 and resp2<1):
                                resp2= resp2 * 100
                                resp2=(np.rint(resp2))
                                return("The {} for {} is {} and it has increased by {} percent since last year.".format(metric.title(),concept.title(),resp1, abs(resp2)))
                            else:
                                resp2=(np.rint(resp2))
                                return("The {} for {} is {} and it has increased by {} percent since last year.".format(metric.title(),concept.title(),resp1, abs(resp2)))
                        
                        else:
                            if re.search("change",metric) is not None:
                                resp3= file.loc[concept,metric]  
                                if (resp3>0 and resp3<1):
                                    resp3= resp3 * 100
                                    resp3=(np.rint(resp3))
                                    if (int(resp3<0)):
                                        
                                        return("There has been {} percent decrease in {} for {} since last year.".format(abs(resp3),metric.title(),concept.title()))
                                else: 
                                    resp3=(round(resp3,3))      
                                    return("There has been {} percent increase in {} for {} since last year.".format(abs(resp3),metric.title(),concept.title()))
            return("Please Check Your Concept Metric Combination")

        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False

parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()


