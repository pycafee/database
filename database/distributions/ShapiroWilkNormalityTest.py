import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def ShapiroWilkNormalityTest(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'ShapiroWilkNormalityTest'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###################################################
    ############ ShapiroWilkNormalityTest #############
    ###################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The Shapiro-Wilk test was not performed. Use the 'shapiro_wilk' method to perform the test.",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O teste de Shapiro-Wilk não foi realizado. Utilize o método 'shapiro_wilk' para realizar o teste.",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Shapiro-Wilk Normality test"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste de Normalidade de Shapiro-Wilk"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    ShapiroWilkNormalityTest()
