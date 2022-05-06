import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_data_in_range(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_data_in_range'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###############################################
    ############ _check_data_in_range #############
    ###############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: out of range',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: fora do intervalo',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text", "{lower}", "Text", "{upper}", "Text", "{value}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{param_name}", "parameter must be a number between", "{lower}", "and", "{upper}", "but we got", "{value}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{param_name}", "deve ser um número entre", "{lower}", "e", "{upper}", "mas obtivemos", "{value}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_data_in_range()
