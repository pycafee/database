import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _sep_checker(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_sep_checker'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #######################################
    ############ _sep_checker #############
    #######################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: length does not match"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: comprimento não confere"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{sep}", "Text", "{len(sep)}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The length of the', "{sep}", "parameter must be equal to 1, but it is", "{len(sep)}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O comprimento do parâmetro', "{sep}", "deve ser igual a 1, mas é ", "{len(sep)}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Hint',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Dica',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _sep_checker()
