import services.data_service as svc
import services.sparql_service as svc_sparql
import numpy as np
import re
import pandas as pd

def run(tableName, columnName):
    """set all column_candidates
        *args: 
                columnName
    """
    candidates_entities_typeObjs(tableName,columnName)
    #candidates_predicates

def candidates_entities_typeObjs(tableName: str, columnName: str):
    """this methods search the instance and match the possible
        entities, then make the storage of the entities in the DB
        *args:
            tableName: str (parameters to get the instances)
            columnName: str
        function:
            -store the entities on the DB ("./services.data_service.register_entites")
        return:
            entityUrisResult: [URI]
    """
    print('start making candidates')
    entityUrisResult = []
    instances = svc.get_instances(tableName, columnName)
    preprocessedInstances = preprocess(instances)
    #CREATE an object - of the sparql service
    sparql = svc_sparql.GetDbpedia()
    #ITERATE for each instance 
    for instance in preprocessedInstances:
        #QUERY the instnace - and take the resultant dictionary of sparql
        auxArray = sparql.search_entity_typeObj(instance)
        entityUrisResult.extend(auxArray)
        #treat_entities_typeObjs(auxArray)
        #STORAGE on the DB the entities - the insertion is in columns
        svc.register_entities(pd.unique(np.transpose(auxArray)[1]))
        svc.register_typeObjs(np.transpose(auxArray)[2],np.transpose(auxArray)[1])
        #print("entity_URI, instance")
        #print(auxArray)
    print(f'finish making canidates from: {tableName}, {columnName}')
    return entityUrisResult

def treat_entities_typeObjs(auxArray):
    auxArray = np.transpose(auxArray)[0]
    return auxArray


def preprocess(instances: []) -> []:
    """make the preproces to the text
        *args:
                instances: []
        output:
                instancesPrepro: []
    """
    return np.array(list(map(lambda v: re.sub(r'\s','_', v) ,instances)))