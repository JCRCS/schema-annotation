
import datetime
import pandas as pd
import services.data_service as svc
import classes.NER.ner as ner
import classes.NEL.nel as nel
import classes.candidates.candidates as candidates



def run():
    print('hollaaaaa!!!!')
    #create_table()
    tableNames = svc.get_tables()
    for iTableName in tableNames:
        columnNames = svc.get_columns(tableName = iTableName)
        for iColumnName in columnNames:
            candidates.run(iTableName, iColumnName)


def create_table():
    print(' creating table')
    tableIn = pd.read_csv(r'C:/ws/schema-annotation-workspace/schema_annotation/Storage/trialCsv.csv')
    table = svc.register_table("soccer3", tableIn.values, tableIn.columns)
    return table

    
    