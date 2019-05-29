from services.sparql_service import *
import services.data_service as svc
import numpy as np

def run(entityUris):
    """this methods search the entity URI and match the possible
        types, then make the storage of the types in the DB
        *args:
            entityUris: []
        function:
            -store the types on the DB
    """
    print('start nel')
    #creates an object of the sparql service
    sparql = GetDbpedia()
    for entityUri in entityUris:
        #take the resultant dictionary of sparql
        auxArray = sparql.search_typeObj(entityUri)
        #storage on the DB the types, the inseartion is in colulmns
        print(svc.register_typeObjs(np.transpose(auxArray)[0],np.transpose(auxArray)[1]) if auxArray != [] else "not find")
        #print("typeObj_URI, entity")
        #print(auxArray)
    print('finish nel')
