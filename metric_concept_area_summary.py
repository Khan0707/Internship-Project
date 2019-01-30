
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

concepts=["baby shop","baby","bebe","bb","candle","candel","candelite","sandal","emacs","first",
"fitness","foot","food","city","fun","box","home","centre.","point","central.","lip",
 "other","iconic","eye","koton","cotton","kitten","lifestyle","style","live","ispsy","hipsy",
"lipsy","lips","max","maths","maps","look","new look","freeze","race","yeast","lease","least",
"rice","forest","sara","express","splash","/","lash","one","sports","sportsone","london","clinics",
"eye","mart","smi","sy","total","shab","sir","mour","tile","mour","sumit"]

areas=["yuriai","uae","you","uei","u a e","ua","urine","hindi","parent","rain","bahrain","buying","egypt","is it","reject","fidget","jet","get","overall","all","mum","kfc",
"damam","jiddah","riyadh","ksa","ks","dammam","the map","jeddah","dhamaal","the mum","dum","wait","kuwait","lebanon","non","oman","man","qatar","tar","gift","kuta","katha","pathar","women","dam","damoh","uidai"]


keywords=["srp","srk",
"shukran revenue penetration",
"shukran revenue",
"shukran penetration revenue",
"ssrp",
"recipe",
"sukran revenue presentation",
"sukran revenue penetration",
"sukran revenue",
"sukran penetration revenue",
"srv",

"average members spend",
"average member spend",
"average members friend",
"average member friend"
"member spend",
"average member"
"average members spent",
"average member spent",
"member spent",
"ams",
"a m s",
"a ms",
"ems",
"ee mm ss",

"ms",
"average spend",
"average spent",
"famous",
 





"number of shukran members",
"shukran members",
"members",
"member",
"shukran member",
"number of shukran member",
"number",
 




"atv",
"average transaction value",
"transaction value",
"etv",
"e tv",
"tv",
"8",
 
"unit per transaction",
"units per transaction",
"you pt",
"your pt",
"upt",
"transaction per units",
"transaction per unit",
"transactions per unit",
"unit for transaction",
"units for transaction",
"u p t",
"up",
 
"new percentage",
"new percentage of customers",
"new customer",
"percentage of new customers",
"new customers",
"percentage of new customer",
"percentage of new customer",

"existing customers",
"existing customer",
 
"percentage of existing customers",
"percentage of existing customer",
"existing customer percentage",
"current customer percentage",
"percentage of current customers",
"percentage of current customer",
"percentage of present customers",
"percentage of present customer",
"current customers percentage",

"testing customers",
"testing customer",
 
"percentage of customers who have churned",
"term percentage",
"churn percentage",
"turn percentage",
"percentage of customer who have churned",
"churn percentage",
"churn rate",
"churn",
"chand percentage",
"percentage of customer who have turned",
"percentage of customer who have chand",
"churn rate for",
"chand",
"chart",
 
"repeat customer",
"repeat customers percentage",
"percentage of repeat customers",
"percentage of repeat customer",
"percentage of repeating customer",
"percentage of repeating customers",
"repeat revenue",
"repeat evenue percentage",
"repeated revenue percentage",
"repeated revenue",
"repeated renew",
"repeated re new",
"repeated avenue",
"repeat renew",
"repeat re new",
"repeat new",
"repeater revenue",
 
"gold customer",
"gold customers",
"gold customer percent",
 
"gold revenue percentage",
"gold revenue percentage",
"revenue from gold customer",
"revenue from gold customers",
"gold revenue",
 
"vintage customer",
"vintage customers",
"wintage customer",
"wintage customers",
"customer vintage",
"customers vintage",
 
"vintage revenue",
"wintage revenue",
"revenue from vintage",
"revenue for vintage",
"vintage review",
"offline customer percentage",
"customers who buy from store",
"customers from store",
"customer from store",
"buy from store",
"customer buy from store",
"offline customer",
"offline active",
"orphan",
 
 
"revenue from offline customers",
"revenue from offline customer",
"store revenue",
"offline customers revenue",
"offline customer revenue",
"offline revenue",
 
 
"percentage of customers who buy online",
"percentage of customer who buy online",
"percentage of online customers",
"percentage of online customer",
"percentage of customers online",
"percentage of customer online",
"online customers",
"online customer",
"online active customers",
"online active customer",
"online customers",
"online customer",
"customer who buy online",
"customers who buy online",
 
"revenue percenatage from online customers",
"revenue percenatage from online customer",
"percenatage of revenue from online customers",
"percenatage of revenue from online customer",
"online revenue percentage",
 
"customers having valid phone number",
"customer having valid phone number",
"customers with valid phone number",
"customer with valid phone number",
"customers with valid number",
"customer with valid number",
"valid mobile customer",
"valid mobile customers",
"customers having valid number",
"customers having valid number",
"phone",
 
 
"customers having valid email",
"customer having valid email",
"customers with valid email",
"customer with valid email",
"customers with valid email",
"customer with valid email",
"valid email customer",
"valid email customers",
"mail",
"male",
"elements",

"enrollment",
"enrollments",
 
 
 
"percentage of high value customer",
"high balu customer",
"high balue customer",
"high value customer",
 
 
"revenue from high value customer",
"high value revenue",
 
 
 
"omni channel revenue",
"omnichannel revenue",
"channel revenue",
 
 
"omni channel customer",
"omnichannel customer",
"channel customer",
 
 
"shukran active customer",
"shukran active",
"Sukran at to customers",
"sukran active customer",
"sukran active",
"shukran app",
"shukran application",
"sukran app",
"sukran application",
 
"download"
]


keys=[x.lower() for x in keywords]

#keylist csv
file1=None
file2=None
# concept=None
# area=None
# metric=None
filename = "C:\\Users\\lmgacoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Mapping files\\keylist.csv"
fileconcept="C:\\Users\\lmgacoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Mapping files\\concept_list.csv"
filearea="C:\\Users\\lmgacoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Mapping files\\territory_list.csv"
#fileoverview="C:\\Users\\lmgcoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Mapping files\\summary.csv"
ct = 0
cp = 0
ac=0
#oc=0

class QueryService(Resource):
    def post(self):
        arg1 = parser.parse_args()
        result = clf.predict(arg1["data"])
        return result


class QueryAnalyzer(object):

    # def closeMatches(patterns, word): 
    #  return(get_close_matches(word, patterns)) 
     

    def predict(self, data):
        global file1
        global file2
        global area
        global concept
        global metric
        global audio
        
        
        file = pd.read_csv("C:\\Users\\lmgacoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Loyality Dashboard\\loyality.csv")
        file.columns= file.columns.map(lambda x:re.sub('\s+',' ',x).strip())
        file=file.drop_duplicates(subset=None,keep='first')
        file=file.set_index('concept')

        file.columns = file.columns.str.rstrip()
        file.columns = file.columns.str.lower()
        file.index = file.index.str.lower()
        
        ###load the keyfil and convert it to lowercase
        keyfile = open(filename , 'r')
        keyfile = (line.lower() for line in keyfile)
        conceptfile=open(fileconcept , 'r')
        conceptfile = (line.lower() for line in conceptfile)
        areafile=open(filearea , 'r')
        areafile = (line.lower() for line in areafile)
        audiofile= pd.read_csv("C:\\Users\\lmgacoeadmin\\Desktop\\Voice_Poc_structured\\Input\\Mapping files\\summary.csv")
        #audio="Highest increase of AMS is in egypt by 40.42 percent and Highest decrease of AMS is in  Uae by 9.49 percent"

        try:
            for i in areas:
                if i in data.lower():
                    for row in csv.reader(areafile,delimiter=','):
                        if row[ac].lower() == i.lower():
                            area=row[1]
                            file1=file.loc[file.territory==area,:]
                            return area.upper();
                    break
                          
                
            for j in concepts:
                
                if j in data.lower():
                    for row in csv.reader(conceptfile,delimiter=','):
                        if row[cp].lower().strip(' ') == j.lower().strip(' '):
                            concept=row[1]
                            file2=file1.loc[(file1.index==concept),:]
                            return concept.upper()
            for k in keys:
                if k  in data.lower():# and terr_flag==1 and concept_flag==1:
                    for row in csv.reader(keyfile,delimiter=','):
                        if row[ct].lower().strip(' ') == k.lower().strip(' '):
                            metric=row[1]
                            if metric=="srp" or metric=="ams" or metric=="churn percentage" or metric=="atv" or metric=="high value revenue":
                            	audio_file=audiofile[(audiofile['metricname'] == metric) & (audiofile['conceptname']==concept)]
                            	audio=audio_file.iloc[0,2]
                            else:
                            	audio="Not Available"

                            
                            
                            if re.search("change",data) is None:
                                resp1= file2.loc[concept,metric]
                                resp1=float(resp1)
                                #return ("{} and {} and {}".format(concept,metric,area))   #####all ok
                                
                                #return ("{} and {} and {}".format(concept,metric,area)) #########ok
                                
                                if (resp1>0 and resp1<1):
                                        resp1= resp1 * 100
                                        resp1=(np.rint(resp1))  
                                else:
                                    resp1=(np.rint(resp1))
                                if re.search("percentage",metric) is None:
                                    resp2 = file2.loc[concept,metric+" percentage change"]
                                    
                                    resp2=float(resp2)
                                else:
                                    resp2 = file2.loc[concept,metric+" change"]
                                    resp2=float(resp2)
                                #return(resp2)    ################################################# ok
                                if (resp2<0 and resp2 >-1):  ### CASE OF negatives     
                                    resp2= resp2 * 100
                                    resp2=(np.rint(resp2))
                                    if metric=="atv" or metric=="ams" or metric=="upt" or metric=="members" or metric=="enrollment":

                                        if metric=="atv" or metric=="ams" :#or :
                                            return ("For {}, the {} for {} is {} AED and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif  metric=="upt":
                                            return ("For {}, the {} for {} is {} units and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif metric=="members":
                                            return ("For {}, the {} for {} are {} (k) and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                        elif metric=="enrollment":
                                            return ("For {}, the {} for {} is {} (k) and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                    else:
                                        return("For {}, the {} for {} is {} percent and it has decreased by {} percentage points since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                    

                                elif(resp2 <= -1): #equal to -1
                                    resp2=(np.rint(resp2))
                                    if metric=="atv" or metric=="ams" or metric=="upt" or metric=="members" or metric=="enrollment":
                                        if metric=="atv" or metric=="ams" :#or :
                                            return ("For {}, the {} for {} is {} AED and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif  metric=="upt":
                                            return ("For {}, the {} for {} is {} units and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif metric=="members":
                                            return ("For {}, the {} for {} are {} (k) and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                        elif metric=="enrollment":
                                            return ("For {}, the {} for {} is {} (k) and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                    else:
                                        return("For {}, the {} for {} is {} percent and it has decreased by {} percentage points since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                    
                    
                                elif (resp2>=0 and resp2<1):     ##### bwetween 0 and 1
                                    resp2= resp2 * 100
                                    resp2=(np.rint(resp2))
                                    if metric=="atv" or metric=="ams" or metric=="upt" or metric=="members" or metric=="enrollment":
                                        if metric=="atv" or metric=="ams" :#or :
                                           return ("For {}, the {} for {} is {} AED and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif  metric=="upt":
                                            return ("For {}, the {} for {} is {} units and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif metric=="members":
                                            return ("For {}, the {} for {} are {} (k) and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                        elif metric=="enrollment":
                                            return ("For {}, the {} for {} is {} (k) and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                    else:
                                        return("For {}, the {} for {} is {} percent and it has increased by {} percentage points since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                else:
                                    resp2=(np.rint(resp2))     ###greater than 1
                                    #return(resp2)
                                    if metric=="atv" or metric=="ams" or metric=="upt" or metric=="members" or metric=="enrollment":

                                        if metric=="atv" or metric=="ams" :#or :
                                            return ("For {}, the {} for {} is {} AED and it has decreased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif  metric=="upt":
                                            return ("For {}, the {} for {} is {} units and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                        elif metric=="members":
                                            return ("For {}, the {} for {} are {} (k) and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))

                                        elif metric=="enrollment":
                                            return ("For {}, the {} for {} is {} (k) and it has increased by {} percent since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                                    else:
                                        return("For {}, the {} for {} is {} percent and it has increased by {} percentage points since last year.\nOverall insight for {} in {} is - {}.".format(area.upper(),metric.upper(),concept.upper(),resp1, abs(resp2),metric.upper(),concept.upper(),audio))
                            else:
                                if re.search("percentage",metric) is not None:
                                    resp3= file2.loc[concept,metric+" change"]  #####
                                    if (resp3>0 and resp3<1):
                                        resp3= resp3 * 100
                                        resp3=(np.rint(resp3))
                                        if (int(resp3<0)):

                                            return("For {}, there has been {} percentage points decrease in {} for {} since last year.".format(area.upper(),abs(resp3),metric.upper(),concept.upper()))
                                    else: 
                                        resp3=(round(resp3,3))      
                                        return("For {}, there has been {} percentage points increase in {} for {} since last year.".format(area.upper(),abs(resp3),metric.upper(),concept.upper()))
###Added
                                # else:
                                #     resp3= file2.loc[concept,metric+" percenatge change"]  
                                #     if (resp3>0 and resp3<1):
                                #         resp3= resp3 * 100
                                #         resp3=(np.rint(resp3))
                                #         if (int(resp3<0)):

                                #             return("For {}, there has been {} percentage points decrease in {} for {} since last year.\nOverall insight for {} in {} is - {}".format(area.upper(),abs(resp3),metric.upper(),concept.upper()))
                                #     else: 
                                #         resp3=(round(resp3,3))      
                                #         return("For {}, there has been {} percentage points increase in {} for {} since last year.\nOverall insight for {} in {} is - {}".format(area.upper(),abs(resp3),metric.upper(),concept.upper()))




            concept=None
            area=None
            metric=None   

            return("Invalid Input")

        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False

parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()