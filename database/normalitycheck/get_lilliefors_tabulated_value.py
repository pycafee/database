import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def get_lilliefors_tabulated_value(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'get_lilliefors_tabulated_value'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #########################################################
    ############ get_lilliefors_tabulated_value #############
    #########################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: value not allowed',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: valor não permitido',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text', "{correction}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'correction' parameter only accepts 'original' or 'abdi-molin' as values, but we got", "{correction}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'correction' aceita apenas 'original' ou 'abdi-molin' como valores, mas recebemos", "{correction}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: very small number of observations',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: número de observações muito pequeno',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text', "{n_rep}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The minimum number of observations to obtain the tabulated value of the Lilliefors test is '4', but we got", "{n_rep}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O número mínimo de observações para obter o valor tabelado do teste de Lilliefors é '4', mas obtivemos", "{n_rep}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [['Text', 'Text', 'Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["LillieforsResult", "tabulate", "alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["LillieforsResultado", "tabelado", "alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    get_lilliefors_tabulated_value()
