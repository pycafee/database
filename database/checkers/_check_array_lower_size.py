import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_array_lower_size(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_array_lower_size'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##################################################
    ############ _check_array_lower_size #############
    ##################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: sample size not accepted',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: Tamanho amostral não aceito',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text", "{value}", "Text," "{array.size}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The minimum sample size for the', "{param_name}", "parameter is", "{value}", "but we got a sample of size", "{array.size}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O tamanho amostral mínimo para o parâmetro', "{param_name}", "é", "{value}", "mas recebemos uma amostra com tamanho", "{array.size}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_array_lower_size()
