

#Import Type
from get_dbpedia import *

#Import Column

#Import Table
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph



class TypeObj(object):
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
    
    def insertType(self, dicInstances = {}):
        """this class is for a easy inserting the types and 
            then make the necessary statistics
            *args
                dicInstances
        """
        # print(dicInstances)



class Types(object):
    """this is a class that manage the dictionary of types
        *args = dicUris         { schema: pandas[columns = [URI, instance]]}
                dicTypes        { schema: {URI : type(text, score, instances, numInstances)}}
        output = filled dicTypes
    """
    def __init__(self, dicUris = {}, dicTypes = {}):
        self.dicUris = dicUris
        self.dicTypes = dicTypes
    
    def generateDicSchema(self):
        if self.dicTypes =={}:
            #create Schemas
            auxArray = [(iSchema, {}) for iSchema in self.dicUris]
            self.dicTypes.update(auxArray)
        #fill types of each schema
        for iSchema in self.dicUris:
            #fill each type with score
            for iUri in pd.unique(self.dicUris[iSchema]["URI"]):
                typeObj = TypeObj()
                typeObj.insertType(self.dicUris[iSchema][self.dicUris[iSchema]["URI"]==iUri])
                # print(self.dicUris[iSchema].groupby("URI").count())



    






class Table2Types(object):
    """This class manage the table and its types
        *args = 
                df          pandas[instance, columns = [schema]]
                dicUris     { schema: pandas[columns = [URI, instance]]}
                sparql
                dicTypes = (Dict of Types)
        methods =   
                    findInstanceTypes( instance)
                    findColTypes( column)
                    findTableTypes( df)
    """
    def __init__(self, df= pd.DataFrame()):
        self.df = df
        self.dicUris = {column: pd.DataFrame([], columns=["URI", "instance"]) for column in df} 
        self.sparql = GetDbpedia()
        self.findTableTypes()
        # self.types = Types(self.dicUris)
        # self.types.generateDicTypes()

        
    
    
    def findInstanceTypes(self, instance):
        auxDict = self.sparql.search(instance)
        auxArray = self.sparql.dict2Types(auxDict, instance)
        auxDf = pd.DataFrame(auxArray,columns= ["URI","instance"])
        return auxDf


    def findColTypes(self, column):
        for instance in self.df[column]:
            # print(instance)
            # print(pd.concat([self.dicUris[column],self.findInstanceTypes(instance)]))
            self.dicUris[column] = pd.concat([self.dicUris[column],self.findInstanceTypes(instance)])
            

    def findTableTypes(self):
        for column in self.df:
            print(column)
            self.findColTypes(column)





            # findColTypes(column)
            # for row in self.df[column]:
            #     print("row" + row)
            #     sparql.search(row)
            #     print(len(resultSparql))
            #     print(resultSparql)



dfAux = pd.DataFrame([["one","bone"],["hundred","knee"]],columns=["prima","seconda"])
table1 = Table2Types(dfAux)
print(table1.df.head())

types = Types(dicUris= table1.dicUris)
types.generateDicSchema()
pass


