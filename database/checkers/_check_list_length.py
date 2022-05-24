import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_list_length(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_list_length'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #############################################
    ############ _check_list_length #############
    #############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: length does not match',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: o tamanho não confere',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [ 
        [['Text', "{param_name}", "Text", "{n}", "Text", "{len(value)}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The ', "{param_name}", "parameter have size equal to", "{n}", "must its size is", "{len(value)}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{param_name}", "deve ter tamanho igual a", "{n}", "mas seu tamanho é", "{len(value)}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_list_length()
