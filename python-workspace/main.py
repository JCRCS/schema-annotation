from get_dbpedia import *
from TypesClass import *
import pandas as pd


# For Jupyter
# import os
# os.getcwd()
# os.chdir('c:\\ws\\schema-annotation-workspace\\schema_annotation\\python-workspace')



def main():
    df_import = pd.read_csv('../Storage/soccer_dataset.csv',index_col=0)
    table = Table2Types(df_import)
    # print(table.df)
    # print(table.types.dicTypes)
    # table.findTableTypes()
    # sparql = GetDbpedia()
    # print(sparql.search("Francesco_Totti"))
    print(table.dicTypes)

main()
print("ciao")