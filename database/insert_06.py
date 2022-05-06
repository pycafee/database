import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def insert_06(database_name="base.db"):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()


    #########################################################################
    ####################   FAZENDO INSERTS Específicos   ####################
    #########################################################################

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    params = [
        ('Sample',),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()


    ################################
    ############ Sample ############
    ################################


    ###########################
    position = 1
    fk_id_function = 1
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Sample',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        # [['ShapiroWilkResultado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['with mean',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        # [['ShapiroWilkResultado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################




















    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()



if __name__ == '__main__':
    insert_06()
    pass
