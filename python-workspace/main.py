from get_dbpedia import *
from TypesClass import *



def main():
    table = Table()
    sparql = GetDbpedia()
    print(sparql.search("Francesco_Totti"))

main()
print("ciao")