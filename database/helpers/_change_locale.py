import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _change_locale(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_change_locale'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #########################################
    ############ _change_locale #############
    #########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: not supported decimal separator.',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: separador decimal não suportado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text", "{decimal_separator}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{param_name}", "parameter accepts only the comma (',') or the dot ('.') as inputs, but we got", "{decimal_separator}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{param_name}", "aceita apenas a vírgula (',') ou o ponto ('.') como inputs, mas recebemos", "{decimal_separator}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{local}", "Text."], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The value passed to 'local' (", "{local}", ") is not supported."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O valor passado para o parãmetro 'local' (", "{local}", ") não é suportado."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _change_locale()
