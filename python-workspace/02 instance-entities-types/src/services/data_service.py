import datetime
import bson
 
from data.instanceObj import InstanceObj
from data.column import Column
from data.table import Table
from data.entity import Entity
from data.typeObj import TypeObj

from typing import List


def register_entities(entitiesUris: []) -> List[Entity]:
    """add a group of entities
        *args:
            entitiesUris: []
        output:
            entities: [URIS]
    """
    entities: List[Entity] = []
    for iEntityUri in entitiesUris:
        entities.append(register_entity(iEntityUri))
    return [entity.entityUri for entity in entities]
    

def register_entity(entityUri: str) -> Entity:
    """ add a entity to the db.
        args*:
            entityUri: str
    """
    entity = Entity()
    entity.entityUri = entityUri
    entity.save()
    return entity

def register_typeObjs(typeObjsUris: [], entitiesUris: []) -> List[TypeObj]:
    """add a group of types
        *args:
            typeObjsUris: []
        output:
            typeObjs: []
    """
    typeObjs: List[TypeObj] = []
    for iEntityUri, iTypeObjUri in zip(entitiesUris, typeObjsUris):
        typeObjs.append(register_typeObj(iEntityUri,iTypeObjUri))
    return typeObjs

def register_typeObj(entityUri: str, typeObjUri: str) -> TypeObj:
    """add a type to a entity
        args*:
            entityUri: str
            typeObjUri: str
    """
    typeObj = TypeObj()
    typeObj.typeObjUri = typeObjUri
    typeObj.save()
    
    entity = Entity.objects(entityUri = entityUri).first()
    entity.type_ids.append(typeObj.id)
    entity.save()

    return typeObj



def register_table(tableName: str, tableContent: [], columnNames: []) -> Table:
    """ add a table to a the db
        args*:
            tableName: str
            tableContent: []
            columnNames: []
    """
    table = Table()
    table.name = tableName
    table.save()

    for iColumn, iColumnName in zip(tableContent.transpose(), columnNames) :
        register_column(table, iColumn, iColumnName)

    return Table

def register_column(table: Table,
                    columnContet: [],
                    columnName: str) -> Table:
    """
    """
    column = Column()
    column.name = columnName
    column.table_id = table.id

    table = Table.objects(id = table.id).first()
    table.columns.append(column)
    table.save()

    for iInstance in columnContet:
        register_instanceObj(   table, 
                                column,
                                iInstance
                            )
    return table

def register_instanceObj(table: Table, 
                        column: Column,
                        instanceObjText: str) -> Table:
    """
    """
    instanceObj = InstanceObj()
    instanceObj.text = str(instanceObjText)
    column.instances.append(instanceObj)
    #**********************************************************fix it!*********************
    #tableId = ""
    # tableId = column.table_id
    # print (f'column.table_id: {tableId}, column.my_metaclass: {column.my_metaclass}.')
    # table = Table.objects(id = tableId).first()
    #column.my_metaclass
    table.save()

    return table

def get_tables() -> []:
    """fetch table names
        *args:
        result:
                tableNames: []
    """

    tables = Table.objects()\
                .only('name')
    return [iTable.name for iTable in tables]

def get_columns(tableName) -> []:
    """fetch column names
        *args: 
                tableName: str
        output:
                columnNames: []
    """
    table = Table.objects(name = tableName).first()
    return [iColumn.name for iColumn in table.columns]

def get_instances(tableName, columnName) -> []:
    """ fetch the instances of a column in a table
        *args:
                tableName: str
                columnName: str
        output:
                instancesNames: []
    """
    table = Table.objects(name = tableName).first()
    
    instancesContent = [
        instance.text
        for column in table.columns 
        for instance in column.instances
        if column.name == columnName]
    return instancesContent







