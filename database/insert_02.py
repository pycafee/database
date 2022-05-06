import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def insert_kolmogorov_smirnov(database_name="base.db"):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = 'kolmogorov_smirnov'

    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###########################################
    ############ KOLMOGORV-SMIRNOV ############
    ###########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    ###########################
    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['KolmogorovSmirnovResult',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['KolmogorovSmirnovResultado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Statistic',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Estatistica',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Tabulated',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Tabelado',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['p_value',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['p_valor',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Conclusion',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Conclusao',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "$Number$", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The sample size must be greater than or equal to 3, but it is', "$Number$", "!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['O tamanho amostral deve ser maior ou igual a 3, mas é', "$Number$", "!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "$Number$", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Data is Normal (at alpha=', "$Number$", "%)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados são Normais (com alfa=', "$Number$", "%)"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "$Number$", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Data is NOT Normal (at alpha=', "$Number$", "%)"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Os dados NÃO são Normais (com alfa=', "$Number$", "!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    insert_kolmogorov_smirnov()
