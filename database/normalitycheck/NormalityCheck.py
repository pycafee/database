import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def NormalityCheck(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'NormalityCheck'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #########################################
    ############ NormalityCheck #############
    #########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The NormalityCheck was not performed yet. Use the 'check' method to perform the test.",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O NormalityCheck ainda não foi realizado. Utilize o método 'check' para realizar o teste.",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["NormalityCheck"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["NormalityCheck"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: value not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: valor não permitido"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [["Text", "{test}", "Text", "{test}", "Text", "{values}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The parameter", "{test}", "does not accept the value", "{test}", "The accepted values are", "{values}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{test}", "não aceita o valor", "{test}", "Os valores aceitos são", "{values}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["UserWarning"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["UserWarning"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The Abdi-Molin test does not support the 'conclusion' parameter"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O teste de Abdi-Molin não suporta o parâmetro 'conclusion'"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The comparison will be made by comparing the test statistic with the respective critical value"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A comparação será feita comparando a estatística do teste com o respectivo valor crítico"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    NormalityCheck()
