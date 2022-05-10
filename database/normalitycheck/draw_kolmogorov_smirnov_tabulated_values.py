import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def draw_kolmogorov_smirnov_tabulated_values(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'draw_kolmogorov_smirnov_tabulated_values'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###################################################################
    ############ draw_kolmogorov_smirnov_tabulated_values #############
    ###################################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Tabulated values of the Kolmogorov Smirnov normality test',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Valores tabelados do teste de normalidade de Kolmogorov Smirnov',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Number of observations',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Número de observações',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Tabulated value',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Valor tabelado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [['Text', "{file_name}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{file_name}", "file has been exported",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O arquivo', "{file_name}", "foi exportado!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    draw_kolmogorov_smirnov_tabulated_values()
