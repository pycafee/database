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
    position = position + 1 #2

    params = [
        [['Text', "{std}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The sample standard deviation (", "{std}", ") is lower than 10E-6, which makes the results inaccurate."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O desvio padrão da amostra (", "{std}", ") é menor que 10E-6, o que torna os resultados imprecisos."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [["Text", "{100*(1-alfa}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Kurtosis is Normal (", "{100*(1-alfa}", "% confidence)",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A Curtose é Normal (", "{100*(1-alfa}", "% de confiança)",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [["Text", "{100*(1-alfa}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Kurtosis is NOT Normal (", "{100*(1-alfa}", "% confidence)",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A Curtose é NÃO Normal (", "{100*(1-alfa}", "% de confiança)",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [["Text", "{kurtosis}", "Text", "{lower}", "Text", "{upper}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the kurtosis (", "{kurtosis}", ") is a value between the lower critical value (", "{lower}", ") and the upper critical value (", "{upper}", "), we have no evidence to reject the null hypothesis that the distribution has kurtosis similar to the kurtosis of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)." ], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a curtose (", "{kurtosis}", ") é um valor entre o valor crítico inferior (", "{lower}", ") e o valor critico superior (", "{upper}", "), não temos evidências para rejeitar a hipótese nula de que a distribuição apresenta curtose similar a curtose de uma distribuição Normal (com ", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [["Text", "{kurtosis}", "Text", "{upper}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the kurtosis (", "{kurtosis}", ") is a value higher than the upper critical value (", "{upper}", "), we have evidence to reject the null hypothesis, and we can say that the distribution does not have kurtosis similar to the kurtosis of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a curtose (", "{kurtosis}", ") é um valor maior do que o valor crítico superior (", "{upper}", "), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta curtose similar a curtose de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [["Text", "{kurtosis}", "Text", "{lower}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the kurtosis (", "{kurtosis}", ") is a value lower than the lower critical value (", "{lower}", "), we have evidence to reject the null hypothesis, and we can say that the distribution does not have kurtosis similar to the kurtosis of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a curtose (", "{kurtosis}", ") é um valor menor do que o valor crítico inferior (", "{lower}", "), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta curtose similar a curtose de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [["Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["KurtosisResult", "Statistics", "Critical", "Alpha", "SkewnessResult"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["ResultadoCurtose", "Estatistica", "Critico", "Alfa", "ResultadoAssimetria" ], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #9

    params = [
        [["Text", "{100*(1-alfa}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Skewness is Normal (", "{100*(1-alfa}", "% confidence)",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A Assimetria é Normal (", "{100*(1-alfa}", "% de confiança)",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #10

    params = [
        [["Text", "{100*(1-alfa}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Skewness is NOT Normal (", "{100*(1-alfa}", "% confidence)",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A Assimetria é NÃO Normal (", "{100*(1-alfa}", "% de confiança)",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #11

    params = [
        [["Text", "{skewness}", "Text", "{lower}", "Text", "{upper}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the skewness (", "{skewness}", ") is a value between the lower critical value (", "{lower}", ") and the upper critical value (", "{upper}", "), we have no evidence to reject the null hypothesis that the distribution has skewness similar to the skewness of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)." ], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a assimetria (", "{skewness}", ") é um valor entre o valor crítico inferior (", "{lower}", ") e o valor critico superior (", "{upper}", "), não temos evidências para rejeitar a hipótese nula de que a distribuição apresenta assimetria similar a assimetria de uma distribuição Normal (com ", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #12

    params = [
        [["Text", "{skewness}", "Text", "{upper}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the skewness (", "{skewness}", ") is a value higher than the upper critical value (", "{upper}", "), we have evidence to reject the null hypothesis, and we can say that the distribution does not have skewness similar to the skewness of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a assimetria (", "{skewness}", ") é um valor maior do que o valor crítico superior (", "{upper}", "), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta assimetria similar a assimetria de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #13

    params = [
        [["Text", "{skewness}", "Text", "{lower}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the calculated statistic for the skewness (", "{skewness}", ") is a value lower than the lower critical value (", "{lower}", "), we have evidence to reject the null hypothesis, and we can say that the distribution does not have skewness similar to the skewness of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatistica calculada para a assimetria (", "{skewness}", ") é um valor menor do que o valor crítico inferior (", "{lower}", "), temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta assimetria similar a assimetria de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #14

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Kurtosis and Skewness measures",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Medidas de Curtose e Assimetria",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    # ---------------------removed due to issues on the p-value -----------------#
    # ###########################
    # position = position + 1 #8
    #
    # params = [
    #     [["Text", "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
    #     [["Since the p-value (", "{p_value}", ") is lower than the adopted significance level (", "{alfa}", "), we have evidence to reject the null hypothesis, and we can say that the distribution does not have kurtosis similar to the kurtosis of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
    #     [["Como o p-valor (", "{p_value}", ") é menor do que o nível de significancia adotado (", "{alfa}", ") , temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição não apresenta curtose similar a curtose de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    # ]
    # for param in params:
    #     func.insert_into_message_message_parts(*param)
    # ###########################
    #
    # ###########################
    # position = position + 1 #9
    #
    # params = [
    #     [["Text", "{p_value}", "Text", "{alfa}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
    #     [["Since the p-value (", "{p_value}", ") is higher than the adopted significance level (", "{alfa}", "), we do not have evidence to reject the null hypothesis, and we can say that the distribution have kurtosis similar to the kurtosis of a Normal distribution (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
    #     [["Como o p-valor (", "{p_value}", ") é maior do que o nível de significancia adotado (", "{alfa}", ") , não temos evidências para rejeitar a hipótese nula, e podemos dizer que a distribuição apresenta curtose similar a curtose de uma distribuição Normal (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    # ]
    # for param in params:
    #     func.insert_into_message_message_parts(*param)
    # ###########################

    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()



if __name__ == '__main__':
    gaussian()
