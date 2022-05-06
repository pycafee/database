import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _flat_list_of_lists(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_flat_list_of_lists'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##############################################
    ############ _flat_list_of_lists #############
    ##############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: not a list of lists"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: não é uma lista de listas"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['At least one element of the', "{param_name}", "list is not a list"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Pelo menos um elemento da lista', "{param_name}", "não é uma lista"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _flat_list_of_lists()
