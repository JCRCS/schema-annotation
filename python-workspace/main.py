from get_dbpedia import *
from TypesClass import *


# For Jupyter
# import os
# os.chdir('c:\\ws\\schema-annotation-workspace\\schema_annotation\\python-workspace')


def main():
    table = Table()
    sparql = GetDbpedia()
    print(sparql.search("Francesco_Totti"))

main()
print("ciao")