import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def draw_density_function(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'draw_density_function'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ################################################
    ############ draw_density_function #############
    ################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text', "{file}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{file}", "file was exported!",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O arquivo", "{file}", "foi exportado!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Key not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Key não aceita"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [["Text", "{param}", "Text", "{scott}", "Text", "{silverman}", "Text", "{bw_method}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{param}", "parameter only accepts", "{scott}", "or", "{silverman}", "as key, but we got", "{bw_method}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{param}", "aceita apenas", "{scott}", "ou", "{silverman}", "como key, mas recebemos", "{bw_method}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [["Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Non-parametric density", "Mean", "Median", "Mode"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Densidade não paramétrica", "Média", "Mediana", "Moda"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Non-parametric density"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Densidade não paramétrica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["UserWaring"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["UserWaring"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The data does not have a mode (all values are unique)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os dados não tem uma moda (todos os valores são únicos)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The data has more than one mode (bimodal or multi-modal distributions tend to be over smoothed)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os dados contém mais de uma moda (distribuições bi ou multi modais tendem a ser muito suavizadas)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
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
    draw_density_function()
