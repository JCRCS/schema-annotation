

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
    def __init__(self, text = "" , instances=[], columns = {}):
        """ constructor of the Type
        """
        self.text = text
        self.score = {}
        self.instances = instances
        # self.numInstances = len(self.instances)
        # self.columns = columns
        # self.numColumns = len(self.numColumns)
    
    def insertType(self, dicUris):
        """this class is for a easy inserting the types and 
            then make the necessary statistics
            *args =
                    dicUris     [columns = [URI, instance]]:pandas
        """
        # if the quantity of dif instances is just 1 the go:
        if len(pd.unique(dicUris.URI))==1:
            self.text = dicUris.URI.values[0]
            self.score.update([("quantityInstances",len(dicUris.URI))]
            )
            self.instances.append(dicUris.instance)
        else:
            print("there are two different types")
        # print(dicInstances)




class Types(object):
    """this is a class that manage the dictionary of types
        *args = dicSchema         { schema: pandas[columns = [URI, instance]]}
                dicTypes        { schema: {URI : type(text, score, instances, numInstances)}}
        output = filled dicTypes
    """
    def __init__(self, dicSchema = {}, dicTypes = {}):
        self.dicSchema = dicSchema
        self.dicTypes = dicTypes
    
    def generateDicSchema(self):
        if self.dicTypes =={}:
            #create Schemas
            auxArray = [(iSchema, {}) for iSchema in self.dicSchema]
            self.dicTypes.update(auxArray)
        #fill types of each schema
        for iSchema in self.dicSchema:
            #fill each type with score
            for iUri in pd.unique(self.dicSchema[iSchema]["URI"]):
                typeObj = TypeObj()
                #insertType( all the pandas of a URI instance, that match with iUri)
                typeObj.insertType(self.dicSchema[iSchema][self.dicSchema[iSchema]["URI"]==iUri])
                self.dicTypes[iSchema].update([(iUri,typeObj)])
                # print(self.dicSchema[iSchema].groupby("URI").count())



    






class Table2Types(object):
    """This class manage the table and its types
        *args = 
                df          pandas[instance, columns = [schema]]
                dicSchema     { schema: pandas[columns = [URI, instance]]}
                sparql
                dicTypes = (Dict of Types)
        methods =   
                    findInstanceTypes( instance)
                    findColTypes( column)
                    findTableTypes( df)
    """
    def __init__(self, df= pd.DataFrame()):
        self.df = df
        self.preprocess()
        self.dicSchema = {column: pd.DataFrame([], columns=["URI", "instance"]) for column in df} 
        self.sparql = GetDbpedia()
        self.findTableTypes()
        self.types = Types(self.dicSchema)
        self.types.generateDicSchema()

        
    
    
    def findInstanceTypes(self, instance):
        auxDict = self.sparql.search(instance)
        auxArray = self.sparql.dict2Types(auxDict, instance)
        auxDf = pd.DataFrame(auxArray,columns= ["URI","instance"])
        return auxDf


    def findColTypes(self, column):
        for instance in self.df[column]:
            # print(instance)
            # print(pd.concat([self.dicSchema[column],self.findInstanceTypes(instance)]))
            self.dicSchema[column] = pd.concat([self.dicSchema[column],self.findInstanceTypes(instance)])
            

    def findTableTypes(self):
        for column in self.df:
            print(column)
            self.findColTypes(column)

    def preprocess(self):
        self.df = self.df.replace(to_replace= "[\s]", value = "_", regex = True)
        print (self.df)




            # findColTypes(column)
            # for row in self.df[column]:
            #     print("row" + row)
            #     sparql.search(row)
            #     print(len(resultSparql))
            #     print(resultSparql)



dfAux = pd.DataFrame([["one","bone"],["hundred","knee"]],columns=["prima","seconda"])
table1 = Table2Types(dfAux)
print(table1.df.head())

# types = Types(dicSchema= table1.dicSchema)
# types.generateDicSchema()
# pass


