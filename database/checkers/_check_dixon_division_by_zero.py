import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_dixon_division_by_zero(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_dixon_division_by_zero'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ########################################################
    ############ _check_dixon_division_by_zero #############
    ########################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error; Division by zero"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{position_1}", "Text", "{x_exp[position_1]}", "Text", "{position_2}", "Text", "{x_exp[position_2]}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The values in positions", "{position_1}", "(", "{x_exp[position_1]}", ") and", "{position_2}", "(", "{x_exp[position_2]}", ") cannot be equal, as this leads to a division by zero error"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os valores nas posições", "{position_1}", "(", "{x_exp[position_1]}", ") e", "{position_2}", "(", "{x_exp[position_2]}", ") não podem ser iguais, pois isto leva a um erro de divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_dixon_division_by_zero()
