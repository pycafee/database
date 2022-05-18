import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def normalitycheck_fit_shapiro_wilk(database_name):

    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #########################################################################
    ####################   FAZENDO INSERTS Específicos   ####################
    #########################################################################

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'normalitycheck_fit_shapiro_wilk'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()


    #########################################################
    ############ normalitycheck_fit_shapiro_wilk ############
    #########################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    ###########################
    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: value not supported',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: valor não suportado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [['Text', "{details}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'details' parameter only accepts 'short' or 'full' as values, but we got", "{details}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'details' aceita apenas 'short' ou 'full' como valores, mas obtivemos", "{details}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [['Text', "{alfa}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The critical value for alpha", "{alfa}", "is not available. The available alpha values are:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O valor crítico para alfa', "{alfa}", "não está disponível. Os valores de alfa disponíveis são:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [['Text', "{critical}", "Text", "{statistic}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since the critical value (', "{critical}", ") <= statistic (", "{statistic}", "), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o valor crítico (', "{critical}", ") <= estatística (", "{statistic}", "), nós NÃO temos evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Shapiro Wilk com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [['Text', "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data is Normal at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados são Normais com', "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [['Text', "{critical}", "Text", "{statistic}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since the critical value (', "{critical}", ") > statistic (", "{statistic}", "), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o valor crítico (', "{critical}", ") > estatística (", "{statistic}", "), nós TEMOS evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Shapiro Wilk com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [['Text', "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data is Not Normal at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados não são Normais com', "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [['Text', "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since p-value (', "{p_value}", ") >= alpha (", "{alfa}", "), we have NO evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o p-valor (', "{p_value}", ") >= alfa (", "{alfa}", "), nós NÃO temos evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Shapiro Wilk com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #9

    params = [
        [['Text', "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since p-value (', "{p_value}", ") < alpha (", "{alfa}", "), we HAVE evidence to reject the hypothesis of data normality, according to the Shapiro Wilk test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o p-valor (', "{p_value}", ") < alfa (", "{alfa}", "), nós TEMOS evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Shapiro Wilk com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #10

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Result"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Resultado"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 ## 11

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Statistic"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Estatistica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 12

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Critical"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Critico"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 13

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["p_value"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["p_valor"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 # 14

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 #15

    params = [
        [['Text', "{conclusion}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'conclusion' parameter only accepts 'critical' or 'p-value' as values, but we got", "{conclusion}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'conclusion' aceita apenas 'critical' ou 'p-value' como valores, mas obtivemos", "{conclusion}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    normalitycheck_fit_shapiro_wilk()
