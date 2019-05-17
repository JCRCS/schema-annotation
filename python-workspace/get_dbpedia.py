from SPARQLWrapper import *
from rdflib import Graph
import simplejson


class GetDbpedia(object):
    def __init__(self, queryInstance = ""):
        self.queryInstances = queryInstance
        self.response = ""
    def search(self, queryInstance = ""):
        self.queryInstances = queryInstance
        sparql = SPARQLWrapper("http://dbpedia.org/sparql", returnFormat= 'json')
        sparql.setQuery("""
        SELECT DISTINCT ?type
        WHERE {
            ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label.
            ?s a ?type.
            ?label bif:contains \""""+ queryInstance +"""\".
        }

        """)

        try :
            sparql.setReturnFormat('json')
            ret = sparql.query()
            auxDict = ret.convert()
        except ValueError as ve:
            return ve
        return auxDict

searcher = GetDbpedia()
print(searcher.search("Andrei_Aleksandrovich_Ovchinnikov"))
        


# sparql.setReturnFormat(N3)
# results = sparql.query().convert()
# g = Graph()
# g.parse(data=results, format="n3")
# print(g.serialize(format='n3'))

# """queries


# SELECT DISTINCT ?label ?teamlabel ?bpLabel ?height ?number
# WHERE{
#     ?s a <http://dbpedia.org/ontology/SoccerPlayer>.
#     ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label .
#     ?s <http://dbpedia.org/ontology/team>   ?team.
#     ?team <http://www.w3.org/2000/01/rdf-schema#label> ?teamlabel .
#     ?s <http://dbpedia.org/ontology/birthPlace> ?birthPlace .
#     ?birthPlace   <http://www.w3.org/2000/01/rdf-schema#label> ?bpLabel.
#     ?s <http://dbpedia.org/ontology/height> ?height .
#     ?s <http://dbpedia.org/ontology/number> ?number .
#     FILTER(langMatches(lang(?label), "EN")) .
#     FILTER(langMatches(lang(?teamlabel), "EN")) .
#     FILTER(langMatches(lang(?bpLabel), "EN")) .
# }



# SELECT DISTINCT ?type
# WHERE {
#     ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label.
#     ?s a ?type.
#     FILTER regex(str(?label), "Totti").
# }LIMIT 100


###############################################33

    # select distinct ?concept ?label 
    # where {
    #     ?concept a <http://www.w3.org/2002/07/owl#Class> .
    #     ?concept rdfs:label ?label .
    #     FILTER(regex(?label, "Totti", "i")) .
    #     FILTER(langMatches(lang(?label),"EN")) .
    # } LIMIT 100

##############################################3

# SELECT ?x WHERE { ?x ?p "cat" }

# DESCRIBE <http://dbpedia.org/resource/The_Lord_of_the_Rings:_Conquest>

# """"
#var = g.serialize()

