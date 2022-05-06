import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def insert_XXX(database_name="base.db"):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()









    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()



if __name__ == '__main__':
    # insert_XXX()
    pass
