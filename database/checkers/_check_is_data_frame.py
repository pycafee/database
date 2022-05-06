import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_is_data_frame(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_is_data_frame'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###############################################
    ############ _check_is_data_frame #############
    ###############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: not a DataFrame',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: não é um DataFrame',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text", "{type(value).__name__}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{param_name}", "parameter must be a DataFrame, but we got a parameter of type", "{type(value).__name__}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{param_name}", "deve ser do tipo DataFrame, mas recebemos um parâmetro do tipo", "{type(value).__name__}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: empty DataFrame',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: DataFrame vazio',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{param_name}", "parameter cannot be an empty DataFrame."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{param_name}", "não pode ser um DataFrame vazio."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_is_data_frame()
