import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _sep_checker():


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
        [['Error: not a string',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: não é uma string',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{sep}", "Text", "{type(value).__name__}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The parameter', "{sep}", "must be a string, but we got:", "{type(value).__name__}", "Hint"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O parâmetro', "{sep}", "deve ser do tipo string, mas recebemos:", "{type(value).__name__}", "Dica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: the length of the string is not equal to 1',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: o tamanho da string não é igual a 1',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{param_name}", "Text", "{len(sep)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The length of the parameter', "{param_name}", "must be equal to 1, but we got", "{len(sep)}", "Hint"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O lenght do parâmetro', "{param_name}", "deve ser igual a 1, mas é", "{len(sep)}", "Dica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
