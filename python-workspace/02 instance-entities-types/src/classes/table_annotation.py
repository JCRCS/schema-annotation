
import datetime
import services.data_service as scv
import pandas as pd

def run():
    print('hollaaaaa!!!!')
    #create_table()
    create_entity()
    create_type()

def 

def create_table():
    print(' creating table')
    tableIn = pd.read_csv(r'C:/ws/schema-annotation-workspace/schema_annotation/Storage/trialCsv.csv')
    table = scv.register_table("soccer3", tableIn.values, tableIn.columns)
    return table

def create_entity():
    print(' creating entity')
    entityUri = input('insert entity')
    entity = scv.register_entity(entityUri)
    return entity

def create_type():
    print('creating type')
    entityUri = input('insert the entity reference: ')
    typeObjUri = input(f'insert the type Uri fo the entity{entityUri}')
    typeObj = scv.register_typeObj(entityUri,typeObjUri)
    return typeObj
    
    