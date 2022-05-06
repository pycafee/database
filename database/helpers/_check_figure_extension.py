import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_figure_extension(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_figure_extension'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##################################################
    ############ _check_figure_extension #############
    ##################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: extension not supported"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: extensão não suportada"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{extension}", "Text", "{param_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{extension}", "extension is not accepted for the", "{param_name}", "parameter"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A extensão", "{extension}", "não é aceita para o parâmetro", "{param_name}", ""], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The current extensions allowed are:',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['As extensões atualmente permitadas são:',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_figure_extension()
