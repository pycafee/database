import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def gaussian(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'gaussian'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ####################################
    ############ gaussian ##############
    ####################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Division by zero/almost zero",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Divisão por zero/quase zero",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{std}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The sample standard deviation (", "{std}", ") is lower than 10E-6, which makes the results inaccurate."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O desvio padrão da amostra (", "{std}", ") é menor que 10E-6, o que torna os resultados imprecisos."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    gaussian()
