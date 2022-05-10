import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def kolmogorov_smirnov_fit(database_name):

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

    func_name = 'kolmogorov_smirnov_fit'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()


    ################################################
    ############ kolmogorov_smirnov_fit ############
    ################################################

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
        [['Text', "{conclusion}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'conclusion' parameter only accepts 'tabulate' or 'p_value' as values, but we got", "{conclusion}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'conclusion' aceita apenas 'tabulate' ou 'p_value' como valores, mas obtivemos", "{conclusion}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

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
        [['Text', "{details}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'details' parameter only accepts 'short' or 'full' as values, but we got", "{details}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'details' aceita apenas 'short' ou 'full' como valores, mas obtivemos", "{details}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Tabulated value not available',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Valor tabelado não disponível',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [['Text', "{alfa}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The tabulated value for alpha", "{alfa}", "is not available. The comparison test will be performed using the p-value."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O valor tabelado para alfa', "{alfa}", "não está disponível. O teste de comparação será realizado utilizando o p-valor."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [['Text', "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since p-value (', "{p_value}", ") >= alpha (", "{alfa}", "), we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o p-valor (', "{p_value}", ") >= alfa (", "{alfa}", "), nós NÃO temos evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Kolmogorov-Smirnov com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [['Text', "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data is Normal at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados são Normais com', "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #9

    params = [
        [['Text', "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since p-value (', "{p_value}", ") < alpha (", "{alfa}", "), we HAVE evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o p-valor (', "{p_value}", ") < alfa (", "{alfa}", "), nós TEMOS evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Kolmogorov-Smirnov com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #10

    params = [
        [['Text', "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Data is Not Normal at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados não são Normais com', "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 #11

    params = [
        [['Text', "{tabulated}", "Text", "{statistic}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since the tabulated value (', "{tabulated}", ") >= statistic (", "{statistic}", "), we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o valor tabelado (', "{p_value}", ") >= estatística (", "{statistic}", "), nós NÃO temos evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Kolmogorov-Smirnov com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 #12

    params = [
        [['Text', "{tabulated}", "Text", "{statistic}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Since the tabulated value (', "{tabulated}", ") < statistic (", "{statistic}", "), we HAVE evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test at a", "{100*(1-alfa)}", "% of confidence level."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Como o valor tabelado (', "{tabulated}", ") < estatística (", "{statistic}", "), nós TEMOS evidências para rejeitar a hipótese de normalidade dos dados, de acordo com o teste de Kolmogorov-Smirnov com", "{100*(1-alfa)}", "% de confiança."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1 #13

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["KolmogorovSmirnovResult"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["ResultadoKolmogorovSmirnov"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Statistic"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Estatistica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Tabulated"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Tabelado"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["p_value"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["p_valor"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)

    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    kolmogorov_smirnov_fit()
