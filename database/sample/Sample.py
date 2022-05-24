import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def Sample(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'Sample'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #################################
    ############ Sample #############
    #################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: data not found"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: resultados não encontrados"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [['Text', "{name}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The calculations have not been performed for this sample yet. Use the 'fit' method to estimate the statistics for", "{name}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os cálculos ainda não foram realizados para esta amostra. Utilize o método 'fit' para estimar as estatísticas da", "{name}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Sample evaluation class"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Class de avaliação de uma amostra"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Sample"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Amostra"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["with mean"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["com média"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 #6

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Mean"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Média"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Variance"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Variância"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Standard deviation"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Desvio padrão"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################


    ###########################
    position = position + 1 #9

    params = [
        [['Text', "{100*(1-alfa)}", "%"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Confidence interval", "{100*(1-alfa)}", "%"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Intervalo de confiança", "{100*(1-alfa)}", "%"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #10

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Coefficient of variation (%)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Coeficiente de variação (%)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #11

    params = [
        [['Text', "{100*(1-self.alfa)}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["with a", "{100*(1-self.alfa)}", "% of confidence level"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["com", "{100*(1-self.alfa)}", "% de confiança"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #12

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Minimum"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Mínimo"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #13

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Q1"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Q1"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #14

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Median"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Mediana"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #15

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Q3"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Q3"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #16

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Maximum"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Máximo"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #17

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Interquartile range"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Distância interquartílica"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    Sample()
