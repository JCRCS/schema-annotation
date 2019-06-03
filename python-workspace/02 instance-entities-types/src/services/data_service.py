import datetime
import bson
from typing import List
import pandas as pd
import re

 
from data.instanceObj import InstanceObj
from data.column import Column
from data.table import Table
from data.entity import Entity
from data.typeObj import TypeObj



def register_entities_typeObjs(instanceObj: InstanceObj, entities_typeObjs_Uris: []) -> (List[Entity], List[TypeObj]):
    """ register entities and typeObjs
        *args:
            entities_typeObjs: []
                table of [instance, entityUri, typeObjUri]
        return:
            entities: List[Entity]
            typeObjs: List[TypeObj]
    """
    entities: List[Entity] = []
    typeObjs: List[TypeObj] = []
    unique_entitiesUris = pd.unique(entities_typeObjs_Uris[1])
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
    for iEntityUri in unique_entitiesUris:
        entity  = register_entity(instanceObj = instanceObj, entityUri = iEntityUri)
        entities.append(entity)
        iEntityUri_indexes = get_indexes(iEntityUri, entities_typeObjs_Uris[1])
        typeObjsUris = list(entities_typeObjs_Uris[2][iEntityUri_indexes])
        for iTypeObjUri in typeObjsUris:
            typeObj = register_typeObj(entity = entity, typeObjUri = iTypeObjUri)
            typeObjs.append(typeObj)
    return entities, typeObjs


def register_entities(entitiesUris: []) -> List[Entity]:
    ##repair (deprecated)
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
    

def register_entity(instanceObj, entityUri: str) -> Entity:
    """ add a entity to the db.
        args*:
            entityUri: str
    """
    entity = Entity()
    entity.table_id = instanceObj.table_id
    entity.column_id = instanceObj.column_id
    entity.instanceObj_id = instanceObj.id
    entity.entityUri = entityUri
    entity.save()
    return entity

def register_typeObjs(typeObjsUris: [], entitiesUris: []) -> List[TypeObj]:
    ##repaiiir (deprecated)
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

def register_typeObj(entity: Entity, typeObjUri: str) -> TypeObj:
    """add a type to a entity
        args*:
            entityUri: str
            typeObjUri: str
    """
    typeObj = TypeObj()
    typeObj.entity_id = entity.id
    typeObj.typeObjUri = typeObjUri
    typeObj.save()
    
    entity = Entity.objects(id = entity.id).first()
    entity.typeObj_ids.append(typeObj.id)
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
    column.id = len(table.columns)
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
    instanceObj.table_id = table.id
    instanceObj.column_id = column.id
    
    instanceObj.text = str(instanceObjText)
    instanceObj.id = len(column.instanceObjs)
    column.instanceObjs.append(instanceObj)
    table.save()

    return table

def get_tables() -> List[Table]:
    """fetch table names
        *args:
        result:
                tableNames: List[Table]
    """

    tables = Table.objects()
    return [iTable for iTable in tables]

def get_columns_from_Table(table: Table) -> List[Column]:
    """fetch column names
        *args: 
                table: Table
        output:
                columnNames: List[Column]
    """
    #table = Table.objects(id = table.id).first()
    columns = table.columns
    #return [iColumn for iColumn in table.columns]
    return columns

# def get_columns_from_tableName(tableName: str) -> List[Column]:
#     """fetch column names
#         *args: 
#                 tableName: str
#         output:
#                 columnNames: []
#     """
#     table = Table.objects(name = tableName).first()
#     return [iColumn.name for iColumn in table.columns]

def get_instances(column: Column) -> List[InstanceObj]:
    """ fetch the instances of a column in a table
        *args:
                tableName: str
                columnName: str
        output:
                instancesNames: []
    """
    # table = Table.objects(id = table.id).first()
    
    # instancesContent = [
    #     instance
    #     for iColumn in column
    #     for iInstance in iColumn.instances
    #     if iColumn == columnName]
    instances = column.instances
    return instances







