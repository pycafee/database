import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def generic(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'generic'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ##################################
    ############ generic #############
    ##################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text', 'Text', 'Text', "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Result", "critical", "alpha", "Statistic"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Resultado", "critico", "alfa", "Estatistica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text', "{test_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{test_name}", "test was not performed yet. Use the 'fit' method to perform the test.",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O teste de", "{test_name}", "não foi realizado. Utilize o método 'fit' para realizar o teste.",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    generic()
