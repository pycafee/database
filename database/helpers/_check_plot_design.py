import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_plot_design(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_plot_design'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #############################################
    ############ _check_plot_design #############
    #############################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: key not found"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: chave não encontrada"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [['Text', "{chave}", "Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The', "{chave}", "key was not found on the supplied 'plot_design' dict"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['A chave', "{chave}", "não foi encontrada no dicionário 'plot_design'",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The following keys are required:',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['As seguintes chaves são necessárias:',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: inconsistent number of keys',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: Número de chaves inconsistente',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [["Text", "{len}", "Text", "{len}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The number of keys of the 'plot_design' dict must be equal to", "{len}", "but it has a size of", "{len}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O número de chaves do dicionário 'plot_design' deve ser igual a", "{len}", "mas seu tamanho é", "{len}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'plot_design' parameter must have these, and only these, keys:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'plot_design' deve ter estas, e apeas estas, chaves:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: not a list"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: não é uma lista"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [["Text", "{key}", "Text", "{type}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The value for the", "{key}", "key must be list, but we got", "{type}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O valor para a chave", "{key}", "deve ser uma lista, mas é do tipo", "{type}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #9

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: size does not match"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: tamanhos não são iguais"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #10

    params = [
        [["Text", "{chave}", "Text", "{len}", "Text", "{len}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The length of the list contained in", "{chave}", "key must be", "{len}", "but we got", "{len}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O comprimento da lista contida na chave", "{chave}", "deve ser", "{len}", "mas seu compriemnto é", "{len}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #11

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["This list must be like:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Esta lista deve ser da seguinte forma:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #12

    params = [
        [["Text",], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: type mismatch"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: os tipos não coincidem"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #13

    params = [
        [["Text", "{i}", "Text", "{chave}", "Text", "{type}", "Text", "{type}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The type of the element", "{i}", "of the key", "{chave}", "must be", "{type}", "but we got", "{type}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O tipo do elemento", "{i}", "da chave", "{chave}", "deve ser", "{type}", "mas é", "{type}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_plot_design()
