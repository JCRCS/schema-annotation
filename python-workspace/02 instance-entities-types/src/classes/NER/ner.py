
import services.sparql_service as svc_sparql
import services.data_service as svc
import numpy as np
import re

def run(tableName: str, columnName: str):
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
    print('start ner')
    entityUrisResult = []
    instances = svc.get_instances(tableName, columnName)
    preprocessedInstances = preprocess(instances)
    #CREATE an object - of the sparql service
    sparql = svc_sparql.GetDbpedia()
    #ITERATE for each instance 
    for instance in preprocessedInstances:
        #QUERY the instnace - and take the resultant dictionary of sparql
        auxArray = sparql.search_entity(instance)
        entityUrisResult.extend(np.transpose(auxArray)[0])
        #STORAGE on the DB the entities - the insertion is in columns
        svc.register_entities(np.transpose(auxArray)[0])
        #print("entity_URI, instance")
        #print(auxArray)
    print('finish ner')
    return entityUrisResult
    


def preprocess(instances: []) -> []:
    """make the preproces to the text
        *args:
                instances: []
        output:
                instancesPrepro: []
    """
    return np.array(list(map(lambda v: re.sub(r'\s','_', v) ,instances)))