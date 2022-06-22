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

    ###########################
    position = position + 1 # 3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: value not supported',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: valor não suportado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [["Text", "{param_name}", "Text", "{list_of_keys}", "Text", "{param_value}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{param_name}", "parameter only accepts the following values", "{list_of_keys}", "but we got", "{param_value}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{param_name}", "aceita apenas os seguintes valores", "{list_of_keys}", "mas recebemos", "{param_value}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Division by zero"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The estimated standard deviation for the dataset is equal to or very close to zero, which caused a division-by-zero error."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O desvio padrão estimado para o conjunto de dados é igual ou muito próximo a zero, o que causou a um erro de divisão por zero."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
