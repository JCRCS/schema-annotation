import services.data_service as svc
import services.sparql_service as svc_sparql
import numpy as np
import re
import pandas as pd

def run(table: svc.Table, column: svc.Column):
    """set all column_candidates
        *args: 
                columnName
    """
    candidates_entities_typeObjs_sparql(table = table, column = column)
    #candidates_predicates

def candidates_entities_typeObjs_sparql(table: svc.Table, column: svc.Column):
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
    instanceObjs = svc.get_instances(column = column)#tableName, columnName)
    #preprocessedInstances = preprocess(instancesObjs)
    #CREATE an object - of the sparql service
    sparql = svc_sparql.GetDbpedia()
    #ITERATE for each instance 
    for iInstanceObj in instanceObjs:
        preprocessedInstanceName = preprocess(iInstanceObj.text)
        #QUERY the instnace - and take the resultant dictionary of sparql
        auxArray = sparql.search_entity_typeObj(preprocessedInstanceName)
        entityUrisResult.extend(auxArray)
        #treat_entities_typeObjs(auxArray)
        #STORAGE on the DB the entities - the insertion is in columns
        auxArray2 = np.transpose(auxArray)
        svc.register_entities_typeObjs(instanceObj = iInstanceObj, entities_typeObjs_Uris = auxArray2)
        # svc.register_entities(entitiesUris = pd.unique(np.transpose(auxArray)[1]))
        # svc.register_typeObjs(typeObjsUris = np.transpose(auxArray)[2], entitiesUris = np.transpose(auxArray)[1])
        #print("entity_URI, instance")
        #print(auxArray)
    print(f'finish making canidates from: {table.name}, {column.name}')
    return entityUrisResult

def treat_entities_typeObjs(auxArray):
    auxArray = np.transpose(auxArray)[0]
    return auxArray


def preprocess(instanceObjText) -> []:
    """make the preproces to the text
        *args:
                instances: []
        output:
                instancesPrepro: []
    """
    #return np.array(list(map(lambda v: re.sub(r'\s','_', v) ,instances)))
    preprocessedInstance = re.sub(r'\s','_', instanceObjText)
    return preprocessedInstance