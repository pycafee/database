import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_forbidden_character(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_forbidden_character'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #####################################################
    ############ _check_forbidden_character #############
    #####################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Character not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Caracter não permitido"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{character}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{character}", "character cannot be used in a filename."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O caractere", "{character}", "não pode ser utilizado em um nome de arquivo."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The characters not allowed are:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os caracteres não permitidos são:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_forbidden_character()
