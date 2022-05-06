import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def shapiro_wilk_to_csv(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'shapiro_wilk_to_csv'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##############################################
    ############ shapiro_wilk_to_csv #############
    ##############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Parameters',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Parametros',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["ShapiroWilkResult"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["ShapiroWilkResultado"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Statistic"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Estatistica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Tabulated"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Tabelado"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["p_value"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["p_valor"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Message"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Mensagem"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Dados"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 9

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Values"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Valores"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    shapiro_wilk_to_csv()
