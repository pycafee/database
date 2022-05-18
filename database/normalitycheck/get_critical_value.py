import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def get_critical_value(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'get_critical_value'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #############################################
    ############ get_critical_value #############
    #############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: very small number of observations',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: número de observações muito pequeno',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text', "{TestName}", "test is", "{n}", "but we got", "{n_rep}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The minimum number of observations to obtain the critical value of the", "{TestName}", "test is", "{n}", "but we got", "{n_rep}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O número mínimo de observações para obter o valor crítico do teste de", "{TestName}", "é", "{n}", "mas obtivemos", "{n_rep}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text', 'Text', 'Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Result", "critical", "alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Resultado", "critico", "alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    get_critical_value()
