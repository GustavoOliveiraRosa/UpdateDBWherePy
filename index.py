from requeriments.connector import *

initialID = int(input("Id Inicial => "))
finalID = int(input("Id Final => "))
table = input("Table =>")
column = input("Coluna =>")
value = input("Valor =>")

while True:
    if initialID <= finalID:

        print(str("UPDATE ")+str(table)+str(" SET ")+str(column)+str("='")+str(value)+str("' where id=")+str(initialID))
        

        initialID = initialID + 1

    else:
        break