import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def TriangularTest(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'TriangularTest'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #########################################
    ############ TriangularTest #############
    #########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Triangular Test to verify if there is a significant difference between two samples that underwent different treatments."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste Triangular para verificar se existe diferença significativa entre duas amostras que sofreram tratamentos diferentes."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Triangular Test to verify if there is a significant difference between two samples that underwent different treatments."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste Triangular para verificar se existe diferença significativa entre duas amostras que sofreram tratamentos diferentes."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    TriangularTest()
