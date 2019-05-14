

#Import Type

#Import Column

#Import Table
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph



class Type(object):
    """This program intends to be manager of the columns,
        Instances and types of the table.
        *args =     text
                    score
                    instances
                    numInstances
                    # columns
                    # numColumns
    """
    def __init__(self, text = "" , instances={}, columns = {}):
        """ constructor of the Type
        """
        self.text = text
        self.score = []
        self.instances = instances
        self.numInstances = len(self.instances)
        # self.columns = columns
        # self.numColumns = len(self.numColumns)

class Column(object):
    """This objects pretend to be each column in the table
    """

class Types(object):
    """organizes the types of a table
    """
    def __init__(self, table = pd.DataFrame()):
        self.dicTypes = { column:"" for column in table}


class Table(object):
    """This class manage the table and its types
        *args = df (Pandas Dataframe)
                type = (Dict of Types)
    """
    def __init__(self, df= pd.DataFrame()):
        self.df = df
        self.types = Types(table = self.df)

    def searchSPARQL(self, instance):

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
            SELECT ?x WHERE { ?x ?p """+instance+""" }
        """)

        sparql.setReturnFormat(N3)
        results = sparql.query().convert()
        print("results")
        print(results)
        # g = Graph()
        # g.parse(data=results, format="n3")
        # print(g.serialize(format='n3'))


    def findTableTypes(self):
        for column in self.df:
            for row in self.df[column]:
                print("row" + row)
                self.searchSPARQL(row)
    


dfAux = pd.DataFrame([["one","bone"],["hundred","knee"]],columns=["0","1"])
table1 = Table(dfAux)
table1.findTableTypes()
print(table1.df.head())
