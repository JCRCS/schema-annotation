
import datetime
import pandas as pd
import services.data_service as svc
import classes.NER.ner as ner
import classes.NEL.nel as nel
import classes.candidates.candidates as candidates



def run():
    print('enter!!!!')
    create_table()
    # tables = svc.get_tables()
    # for iTable in tables:
    #     columns = svc.get_columns_from_Table(table = iTable)
    #     for iColumn in columns:
    #         candidates.run(iTable, iColumn)


def create_table():
    print(' creating table')
    tableIn = pd.read_csv(r'C:/ws/schema-annotation-workspace/schema_annotation/Storage/trialCsv.csv')
    table = svc.register_table("soccer3", tableIn.values, tableIn.columns)
    return table

    
    