from SPARQLWrapper import *
from rdflib import Graph
import simplejson
from urllib.parse import quote_plus


class GetDbpedia(object):
    def __init__(self, queryTypeObj = ""):
        self.queryInstances = queryTypeObj
        self.response = ""

    def search_typeObj(self, queryTypeObj = ""):
        self.queryInstances = queryTypeObj
        print ("entity to query: "+queryTypeObj)
        url = queryTypeObj
        encoded_url = quote_plus(url, safe= '/:')
        sparql = SPARQLWrapper("http://dbpedia.org/sparql", returnFormat= 'json')
        sparql.setQuery(
            u"""
            SELECT DISTINCT ?type
            WHERE {
                <%s> a ?type.
            }""" % encoded_url
            )

        try :
            sparql.setReturnFormat('json')
            ret = sparql.query()           
            auxDict = ret.convert()
        except:
            return []
        #RETURN in an Array the types
        return self.dict2Array_typeObj(auxDict, queryTypeObj)

    
    def search_entity(self, queryInstance = ""):
        self.queryInstances = queryInstance
        print ("instance to query: "+queryInstance)
        url = queryInstance
        encoded_url = quote_plus(url, safe= '/:')
        sparql = SPARQLWrapper("http://dbpedia.org/sparql", returnFormat= 'json')
        sparql.setQuery(
            u"""
            SELECT DISTINCT ?s
            WHERE {
                ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label.
                ?label bif:contains "%s".

            }""" % encoded_url
            )

        try :
            sparql.setReturnFormat('json')
            ret = sparql.query()
            auxDict = ret.convert()
        except:
            print ("error")
            return []
        #RETURN in an Array the types
        return self.dict2Array_entity(auxDict, queryInstance)
        
    def dict2Array_typeObj(self, resultDict, entity):
        """this is a method to convert the resultant dictionary of sparql
            to a array that only apears the result in an Array.
            *args:
                resultDict: {result: bindings: #: type: value:}
                entity: str (the entity that map all the result)
            return:
                entitiesResult: [URI, entity]
        """
        return [[iType["type"]["value"], entity] for iType in resultDict["results"]["bindings"]]

    def dict2Array_entity(self, resultDict, instance):
        """this is a method to convert the resultant dictionary of sparql
            to a array that only apears the result in an Array.
            *args:
                resultDict: {result: bindings: #: s: value:}
                instance: str (the instance that map all the result)
            return:
                entitiesResult: [URI, instance]
        """
        return [[iType["s"]["value"], instance] for iType in resultDict["results"]["bindings"]]