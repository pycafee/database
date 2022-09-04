import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def StudentDistribution(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'StudentDistribution'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ################################################
    ############ StudentDistribution ###############
    ################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: Key not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: Key não aceita"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [["Text", "{which}", "Text", "{bilateral}", "Text", "{unilateral}", "Text", "{which}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{which}", "parameter only accepts", "{bilateral}", "or", "{unilateral}", "as key, but we got", "{which}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{which}", "aceita apenas", "{bilateral}", "ou", "{unilateral}", "como key, mas recebemos", "{which}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Probability density"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Densidade de probabilidade"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 4

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student's $t$"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["$t$ de Student"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 5

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: interval not allowed"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: intevalo não permitido"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 6

    params = [
        [["Text", "{interval}", "Text", "{interval[0] > interval[1]}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The first element of the", "{interval}", "parameter must be lower than its second element, but", "{interval[0] > interval[1]}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O primeiro elemento do parâmetro", "{interval}", "deve ser menor do que o seu segundo elemento, mas", "{interval[0] > interval[1]}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 7

    params = [
        [["Text", "{interval}", "Text", "{interval[0] > interval[1]}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The first element of the", "{interval}", "parameter must be lower than its second element, but they are equal", "{interval[0] = interval[1]}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O primeiro elemento do parâmetro", "{interval}", "deve ser menor do que o seu segundo elemento, mas eles são iguais", "{interval[0] = interval[1]}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 8

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["UserWaring"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["UserWaring"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 9

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The intervals are not symmetrical! This causes the graph to be shifted!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os intervalos não são simétricos! Isto faz com que o gráfico fique deslocado!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 10

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Rejection region"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Região de rejeição"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 11

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Acceptance region"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Região de aceitação"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 12

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student's t distribution"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Distribuição t de Student"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 13

    params = [
        [["Text", "Text", "Text", "Text", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Student", "Upper", "Lower", "Alpha", "Distribution"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Student", "Superior", "Inferior", "Alfa", "Distribuicao"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 14

    params = [
        [["Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A média (", "{mean}", ") é igual a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 15

    params = [
        [["Text", "{statistic}", "Text", "{critical_low},{Critical_high}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is a number between the critical values (", "{critical_low},{Critical_high}", "), there is no evidence to reject the null hypothesis, and we can say that the mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é um número entre os valores críticos (", "{critical_low},{Critical_high}", ") não existem evidências para rejeitar a hipótese nula, e podemos dizer que a média (", "{mean}", ") é igual a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 16

    params = [
        [["Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The mean (", "{mean}", ") is different from the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A média (", "{mean}", ") é diferente da constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 17

    params = [
        [["Text", "{statistic}", "Text", "{critical_high}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is higher than the upper critical value (", "{critical_high}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is different from the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico superior (", "{critical_high}", ") temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é diferente da constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 18

    params = [
        [["Text", "{statistic}", "Text", "{critical_low}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is lower than the lower critical value (", "{critical_low}", "),  we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is different from constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico inferior (", "{critical_low}", ") temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é diferente da constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 19

    params = [
        [["Text", "{p_value}", "Text", "{alfa}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the p-value (", "{p_value}", ") is lower than the adopted significance level (", "{alfa}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is different from the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o p-valor (", "{p_value}", ") é menor do que o nível de significância adotado (", "{alfa}", "),  temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é diferente da constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 20

    params = [
        [["Text", "{p_value}", "Text", "{alfa}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the p-value (", "{p_value}", ") is higher than the adopted significance level (", "{alfa}", "), we do not have evidence to reject the hypothesis of equality between the means, and we can say that the mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o p-valor (", "{p_value}", ") é maior do que o nível de significância adotado (", "{alfa}", "), nós não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (", "{mean}", ") é igual a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 21

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["OneSampleStudentComparison", "statistic", "critical", "p_value", "alpha"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["OneSampleStudentComparison", "estatistica", "critico", "p_valor", "alfa"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 22

    params = [
        [["Text", "{x_exp.mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The mean (", "{x_exp.mean}", ") is higher than the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A média (", "{x_exp.mean}", ") é maior do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 # 23

    params = [
        [["Text", "{statistic}", "Text", "{critical.Lower}", "Text", "{value}", "Text", "{x_exp.mean()}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is higher than the lower critical value (", "{critical.Lower}", "), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico inferior (", "{critical.Lower}", "), não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (", "{mean}", ") é igual a constante (", "{value}",  ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 24

    params = [
        [["Text", "{statistic}", "Text", "{critical.Lower}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is lower than the upper critical value (", "{critical.Lower}", "), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico superior (", "{critical.Lower}", "), não temos evidências para rejeitar a hipótese nula de igualdade entre a médias, e podemos dizer que a média (", "{mean}", ") é igual a constante (", "{value}",  ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 25

    params = [
        [["Text", "{p_value}", "Text", "{alfa}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the p-value (", "{p_value}", ") is lower than the adopted significance level (", "{alfa}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is higher than the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o p-valor (", "{p_value}", ") é menor do que o nível de significância adotado (", "{alfa}", "), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é maior do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 26

    params = [
        [["Text", "{p_value}", "Text", "{alfa}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the p-value (", "{p_value}", ") is higher than the adopted significance level (", "{alfa}", "), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (", "{mean}", ") is equal to the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o p-valor (", "{p_value}", ") é maior do que o nível de signficância adotado (", "{alfa}", "), não temos evidências para rejeitar a hipótese nula de igualdade entre as médias, e podemos dizer que a média (", "{mean}", ") é igual a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 27

    params = [
        [["Text", "{value}", "Text", "{mean}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The constant (", "{value}", ") and the mean (", "{mean}", ") are exactly the same"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A constante (", "{value}", ") e a média (", "{mean}", ") são exatamente iguais"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 # 28

    params = [
        [["Text", "{x_exp.mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The mean (", "{x_exp.mean}", ") is lower than the constant (", "{}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A média (", "{x_exp.mean}", ") é menor do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 29

    params = [
        [["Text", "{statistic}", "Text", "{critical[1]}", "Text", "{x_exp.mean()}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is lower than the lower critical value (", "{critical[1]}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{x_exp.mean()}", ") is lower than the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico inferior (", "{critical[1]}", "), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{x_exp.mean()}", ") é menor do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 30

    params = [
        [["Text", "{p_value}", "Text", "{alfa}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the p-value (", "{p_value}", ") is lower than the adopted significance level (", "{alfa}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is lower than the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como o p-valor (", "{p_value}", ") é menor do que o nível de significância adotado (", "{alfa}", "), temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é menor do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 31

    params = [
        [["Text", "{param_name}", "Text", "{critical}", "Text", "{p-value}", "Text", "{comparison}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{param_name}", "parameter only accepts the keys", "{critical}", "or", "{p-value}", "but we got", "{comparison}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro", "{param_name}", "aceita como chave apenas", "{critical}", "ou", "{p-value}", "mas recebemos", "{comparison}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 # 32

    params = [
        [["Text", "{statistic}", "Text", "{critical_high}", "Text", "{mean}", "Text", "{value}", "Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Since the test statistic (", "{statistic}", ") is higher than the upper critical value (", "{critical_high}", "), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (", "{mean}", ") is higher than the constant (", "{value}", ") (with", "{100*(1-alfa)}", "% confidence)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico superior (", "{critical_high}", ") temos evidências para rejeitar a hipótese nula de igualdade das médias, e podemos dizer que a média (", "{mean}", ") é maior do que a constante (", "{value}", ") (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 33

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: conflicting parameters"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: parâmetros conflitantes"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 34

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Parameters 'x_exp' and 'params' cannot be of type 'None' at the same time."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os parâmetros 'x_exp' e 'params' não podem ser do tipo 'None' ao mesmo tempo."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 35

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: incompatible sample size"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: tamanho amostral incompatível"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 36

    params = [
        [["Text", "{names[0]}", "Text", "{names[1]}", "Text", "{names[0]}", "Text", "{n_1}", "Text", "{names[1]}", "Text", "{n_2}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The sample size of", "{names[0]}", "and", "{names[1]}", "must be equal, but the number of samples from", "{names[0]}", "is equal to", "{n_1}", ", while the number of samples from ", "{names[1]}", "is equal to", "{n_2}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O tamanho amostral de", "{names[0]}", "e", "{names[1]}", "deve ser igual, mas o número de amostras de", "{names[0]}", "é igual a", "{n_1}", ", enquanto que o número de amostras de", "{names[1]}", "é igual a", "{n_2}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 37

    params = [
        [["Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The paired samples are equal (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["As amostras pareadas são iguais (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 38

    params = [
        [["Text", "{statistic}", "Text", "{low,high}", "Text", "{name_1}", "({mean_1})", "Text", "{name_2}", "({mean_2})", "Text", "{100*(1-alfa)}", "Text", "Text", "{value}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["As the test statistic (", "{statistic}", ") is a number between the critical values (", "{low,high}", "), we have no evidence to reject the null hypothesis of equality between the means of paired samples", "{name_1}", "({mean_1})", "and", "{name_2}", "({mean_2})", "(with", "{100*(1-alfa)}", "% confidence)", "and they don't differ by", "{value}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é um número entre os valores críticos (", "{low,high}", "), não temos evidências para rejeitar a hipótese nula de igualdade entre as médias das amostras pareadas", "{name_1}", "({mean_1})", "e", "{name_2}", "({mean_2})", "(com", "{100*(1-alfa)}", "% de confiança)", "e elas não diferem em", "{value}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 39

    params = [
        [["Text", "{100*(1-alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The paired samples are different (with", "{100*(1-alfa)}", "% confidence)."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["As amostras pareadas são diferentes (com", "{100*(1-alfa)}", "% de confiança)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 40

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{name_1}", "{mean_1}", "Text", "{name_2}", "{mean_2}", "Text", "{100*(1-alfa)}", "Text", "Text", "{value}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["As the test statistic (", "{statistic}", ") is higher than the upper critical value (", "{critical}", "), we have evidence to reject the null hypothesis of equality between the means of the paired samples. Thus, sample", "{name_1}", "{mean_1}", "is different from sample", "{name_2}", "{mean_2}", "(with", "{100*(1-alfa)}", "% confidence)", "and they differ by", "{value}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é maior do que o valor crítico superior (", "{critical}", "), temos evidências para rejeitar a hipótese nula de igualdade entre as médias das amostras pareadas. Assim, a amostra", "{name_1}", "{mean_1}", "é diferente da amostra", "{name_2}", "{mean_2}", "(com", "{100*(1-alfa)}", "% de confiança)", "e elas diferem em", "{value}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 # 41

    params = [
        [["Text", "{statistic}", "Text", "{critical}", "Text", "{name_1}", "{mean_1}", "Text", "{name_2}", "{mean_2}", "Text", "{100*(1-alfa)}", "Text", "Text", "{value}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["As the test statistic (", "{statistic}", ") is lower than the lower critical value (", "{critical}", "), we have evidence to reject the null hypothesis of equality between the means of the paired samples. Thus, sample", "{name_1}", "{mean_1}", "is different from sample", "{name_2}", "{mean_2}", "(with", "{100*(1-alfa)}", "% confidence)", "and they differ by", "{value}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Como a estatística do teste (", "{statistic}", ") é menor do que o valor crítico inferior (", "{critical}", "), temos evidências para rejeitar a hipótese nula de igualdade entre as médias das amostras pareadas. Assim, a amostra", "{name_1}", "{mean_1}", "é diferente da amostra", "{name_2}", "{mean_2}", "(com", "{100*(1-alfa)}", "% de confiança)", "e elas diferem em", "{value}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br # pt-br
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
    StudentDistribution()
