import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def outliers(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'outliers'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###################################
    ############ outliers #############
    ###################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text", "Text", "{which}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: key not supported", "The 'which' parameter only accepts 'min' or 'max' as keys, be we got", "{which}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: chave não suportada", "O parâmetro 'which' aceita apenas 'min' or 'max' como chaves, mas recebemos", "{which}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The dataset has no outliers"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O conjunto de dados não tem outliers"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The dataset has outliers"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O conjunto de dados tem outliers"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["ZScore's test for outlier detection"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste Z para detecção de outliers"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    outliers()
