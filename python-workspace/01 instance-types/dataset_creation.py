from SPARQLWrapper import *
from rdflib import Graph
import simplejson
import pandas as pd

sparql = SPARQLWrapper("http://dbpedia.org/sparql", returnFormat= 'json')
sparql.setQuery("""
SELECT DISTINCT ?label ?teamlabel ?bpLabel ?height ?number
WHERE{
    ?s a <http://dbpedia.org/ontology/SoccerPlayer>.
    ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label .
    ?s <http://dbpedia.org/ontology/team>   ?team.
    ?team <http://www.w3.org/2000/01/rdf-schema#label> ?teamlabel .
    ?s <http://dbpedia.org/ontology/birthPlace> ?birthPlace .
    ?birthPlace   <http://www.w3.org/2000/01/rdf-schema#label> ?bpLabel.
    ?s <http://dbpedia.org/ontology/height> ?height .
    ?s <http://dbpedia.org/ontology/number> ?number .
    FILTER(langMatches(lang(?label), "EN")) .
    FILTER(langMatches(lang(?teamlabel), "EN")) .
    FILTER(langMatches(lang(?bpLabel), "EN")) .
}
""")

try :
    sparql.setReturnFormat('json')
    ret = sparql.query()
    soccerDict = ret.convert()
except ValueError as ve:
    print(ve)

######################### making the table ####################3

auxDict = soccerDict["results"]["bindings"]
soccer = pd.DataFrame()
for columns in soccerDict["head"]["vars"]:
    print (columns)
    soccer[columns] =[out[columns]["value"] for out in auxDict]	


auxArr = [ list(soccer[soccer.label == val].iloc[0]) for val in soccer.label.unique()]
auxDf = pd.DataFrame(auxArr)
auxDf.columns = soccer.columns
soccer = auxDf

soccer.to_csv(r'C://ws/schema-annotation-workspace/schema_annotation/Storage/soccer_dataset.csv',encoding='utf-8-sig')