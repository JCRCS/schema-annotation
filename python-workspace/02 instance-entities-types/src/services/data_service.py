import datetime
import bson
 
from data.instanceObj import InstanceObj
from data.column import Column
from data.table import Table
from data.entity import Entity
from data.typeObj import TypeObj

def register_entity(entityUri: str) -> Entity:
    """ add a entity to the db.
        args*:
            entityUri: str
    """
    entity = Entity()
    entity.entityUri = entityUri
    entity.save()
    return entity



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


