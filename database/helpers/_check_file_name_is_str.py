import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_file_name_is_str(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_file_name_is_str'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##################################################
    ############ _check_file_name_is_str #############
    ##################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: not a string"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: não é uma string"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{type}",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The file name must be a string, but we got", "{type}", ], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O nome do arquivo deve ser uma string, mas é do tipo', "{type}",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: empty string',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: string vazia',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The file name cannot be empty!',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O nome do arquivo não pode ser vazio!',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_file_name_is_str()
