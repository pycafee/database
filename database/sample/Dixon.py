import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def Dixon(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'Dixon'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ################################
    ############ Dixon #############
    ################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: ratio not allowed',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: ratio não permitido',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [["Text", "{ratio}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'ratio' parameter does not accept the key", "{ratio}", "The accepted keys are the following"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'ratio' não aceita a chave", "{ratio}", "As chaves aceitas são as seguintes:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [["Text", "{x_exp[0]}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The lower value (", "{x_exp[0]}", ") perhaps be an outlier (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O valor inferior (", "{x_exp[0]}", ") talvez seja um outlier (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [["Text", "{q_low}", "Text", "{critical}", "Text", "{x_exp[0]}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic value (", "{q_low}", ") is higher than the critical value (", "{critical}", "), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the lower value (", "{x_exp[0]}", ") is an outlier (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o valor da estatistica do teste (", "{q_low}", ") é maior do que o valor crítico (", "{critical}", "), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor inferior (", "{x_exp[0]}", ") seja um outlier (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [["Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data do not have outliers (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os dados não apresentam outliers (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text", "{q_low}", "Text", "{critical}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic value (", "{q_low}", ") is lower than the critical value (", "{critical}", "), we have no evidence to reject the null hypothesis that the sample does not contain outliers (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o valor da estatistica do teste (", "{q_low}", ") é menor do que o valor crítico (", "{critical}", "), não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [["Text", "{x_exp[-1]}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The upper value (", "{x_exp[-1]}", ") perhaps be an outlier (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O valor superior (", "{x_exp[-1]}", ") talvez seja um outlier (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [["Text", "{q_upper}", "Text", "{critical}", "Text", "{x_exp[0]}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic value (", "{q_upper}", ") is higher than the critical value (", "{critical}", "), we have evidence to reject the null hypothesis that the sample does not contain outliers, and perhaps the upper value (", "{x_exp[-1]}", ") is an outlier (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o valor da estatistica do teste (", "{q_upper}", ") é maior do que o valor crítico (", "{critical}", "), temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers, e talvez o valor superior (", "{x_exp[-1]}", ") seja um outlier (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 9

    params = [
        [["Text", "Text", "{which}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: key not supported", "The 'which' parameter only accepts 'min' or 'max' as keys, be we got", "{which}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: chave não suportada", "O parâmetro 'which' aceita apenas 'min' or 'max' como chaves, mas recebemos", "{which}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 10

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Division by zero"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 11

    params = [
        [["Text", "{position_1}", "Text", "{x_exp[position_1]}", "Text", "{position_2}", "Text", "{x_exp[position_2]}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The values in positions", "{position_1}", "(", "{x_exp[position_1]}", ") and", "{position_2}", "(", "{x_exp[position_2]}", ") cannot be equal, as this leads to a division by zero error"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os valores nas posições", "{position_1}", "(", "{x_exp[position_1]}", ") e", "{position_2}", "(", "{x_exp[position_2]}", ") não podem ser iguais, pois isto leva a um erro de divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 12

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Dixon's test for outlier detection"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste de Dixon para detecção de outliers"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    Dixon()
