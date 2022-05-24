import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def StudentDistribution(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'StudentDistribution'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ################################################
    ############ StudentDistribution ###############
    ################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Key not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Key não aceita"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [["Text", "{which}", "Text", "{bilateral}", "Text", "{unilateral}", "Text", "{which}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{which}", "parameter only accepts", "{bilateral}", "or", "{unilateral}", "as key, but we got", "{which}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{which}", "aceita apenas", "{bilateral}", "ou", "{unilateral}", "como key, mas recebemos", "{which}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Probability density"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Densidade de probabilidade"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student's $t$"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["$t$ de Student"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: interval not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: intevalo não permitido"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text", "{interval}", "Text", "{interval[0] > interval[1]}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The first element of the", "{interval}", "parameter must be lower than its second element, but", "{interval[0] > interval[1]}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O primeiro elemento do parâmetro", "{interval}", "deve ser menor do que o seu segundo elemento, mas", "{interval[0] > interval[1]}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [["Text", "{interval}", "Text", "{interval[0] > interval[1]}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The first element of the", "{interval}", "parameter must be lower than its second element, but they are equal", "{interval[0] = interval[1]}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O primeiro elemento do parâmetro", "{interval}", "deve ser menor do que o seu segundo elemento, mas eles são iguais", "{interval[0] = interval[1]}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["UserWaring"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["UserWaring"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 9

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The intervals are not symmetrical! This causes the graph to be shifted!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os intervalos não são simétricos! Isto faz com que o gráfico fique deslocado!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 10

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Rejection region"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Região de rejeição"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 11

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Acceptance region"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Região de aceitação"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 12

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student's t distribution"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Distribuição t de Student"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 13

    params = [
        [["Text", "Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student", "Higher", "Lower", "Alpha", "Distribution"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Student", "Superior", "Inferior", "Alfa", "Distribuicao"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
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
    StudentDistribution()
