import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def LanguageManagement(database_name):


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

    func_name = 'LanguageManagement'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()


    ############################################
    ############ LanguageManagement ############
    ############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    ###########################
    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: language not valid"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: idioma não válido"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [["Text", "{language}", "Text", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{language}", " language is not yet available.", "The available languages are:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma", "{language}", "ainda não esta disponível.", "Os idiomas disponíveis são:",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{_func_name}", "Text", "{language}", "Text", "{_func_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The function", "{_func_name}", "has no translation for language", "{language}", "The languages available for", "{_func_name}", "are", ], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A função", "{_func_name}", "não tem tradução para o idioma ", "{language}", "Os idiomas disponíveis para ", "{_func_name}", "são", ], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{language}",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["If you are interested, you can contribute with the translation to the language", "{language}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Caso tenha interesse, você pode contribuir com a tradução para o idioma", "{language}" ], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{self.language}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The current language is:", "{self.language}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma atual é:", "{language}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    LanguageManagement()
