import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def Grubbs(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'Grubbs'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #################################
    ############ Grubbs #############
    #################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: kind not allowed',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: kind não permitido',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 2

    params = [
        [["Text", "{ratio}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'kind' parameter does not accept the key", "{kind}", "The accepted keys are the following"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'kind' não aceita a chave", "{kind}", "As chaves aceitas são as seguintes:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: alpha not found',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: alfa não encontrado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Grubbs's test for outlier detection"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Teste de Grubbs para detecção de outliers"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The sample standard deviation cannot be equal to zero, as this causes division by zero error."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O desvio padrão da amostra não pode ser igual a zero, pois isto causa em erro de divisão por zero"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The data does not have outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os dados não contém outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["As the test statistic (", "{statistic}", ") is lower than the critical value (", "{critical}", "), we have no evidence to reject the null hypothesis that the sample does not contain outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico (", "{critical}", "), nós não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [["Text", "{outlier}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The sample", "{outlier}", "perhaps be an outlier (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A amostra", "{outlier}", "talvez seja um outlier (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 9

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{outlier}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is higher than the critical value (", "{critical}", "), we have evidence to reject the null hypothesis, and perhaps sample", "{outlier}", "is an outlier (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico (", "{critical}", "), temos evidências para rejeitar a hipótese nula, e talvez a amostra", "{outlier}", "seja um outlier (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 10

    params = [
        [["Text", "{outlier}", "Text", "{outlier}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Samples", "{outlier}", "and", "{outlier}", "may be outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["As amostras", "{outlier}", "e", "{outlier}", "talvez sejam outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 11

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{outlier}", "Text", "{outlier}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is lower than the critical value (", "{critical}", "), we have evidence to reject the null hypothesis, and perhaps sample", "{outlier}", "and", "{outlier}", "are outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico (", "{critical}", "), temos evidências para rejeitar a hipótese nula, e talvez aa amostras", "{outlier}", "e", "{outlier}", "sejam outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 12

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["As the test statistic (", "{statistic}", ") is higher than the critical value (", "{critical}", "), we have no evidence to reject the null hypothesis that the sample does not contain outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico (", "{critical}", "), nós não temos evidências para rejeitar a hipótese nula de que a amostra não contém outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 13

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{outlier}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is higher than the critical value (", "{critical}", "), we have evidence to reject the null hypothesis, and perhaps samples", "{outlier}", "and", "{outlier}", "are outliers (", "{100*(1-alfa)}", "% confidence level)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico (", "{critical}", "), temos evidências para rejeitar a hipótese nula, e talvez as amostras", "{outlier}", "e", "{outlier}", "sejam outliers (", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    Grubbs()
