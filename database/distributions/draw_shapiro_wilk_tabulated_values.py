import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def draw_shapiro_wilk_tabulated_values(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'draw_shapiro_wilk_tabulated_values'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #############################################################
    ############ draw_shapiro_wilk_tabulated_values #############
    #############################################################

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
        [['*the critical value for alpha equal to 0.99 with 30 observations probably has a typo. The correct value is probably 0.990 instead of 0.900.',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['*o valor crítico para alfa igual a 0,99 com 30 observações provavelmente tem um erro de digitação. O valor correto provavelmente é 0,990 em vez de 0,900.',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Tabulated values of the Shapiro Wilk normality test',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Valores tabelados do teste de normalidade de Shapiro Wilk',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    draw_shapiro_wilk_tabulated_values()
