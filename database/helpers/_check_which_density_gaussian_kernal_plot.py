import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _check_which_density_gaussian_kernal_plot(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_check_which_density_gaussian_kernal_plot'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ####################################################################
    ############ _check_which_density_gaussian_kernal_plot #############
    ####################################################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: value not acceptable"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: valor não aceitável"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [['Text', "{word}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'which' parameter does not accepts the character", "{word}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro 'which' não aceita o caractere", "{word}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [['Text'], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["This parameter only accepts the following keys:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Este parâmetro aceita apenas as seguintes chaves:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['The keys must be separated by a comma (',')',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['As chaves devem ser separadas por uma vírgula (',')',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [['Error: no key match found',], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [['Erro: nenhuma correspondência de chave encontrada',], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [['Text', "{value}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{value}", "key is not allowed",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A chave", "{value}", "não é permitida"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The accepted keys are:",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["As chaves aceitas são:",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Error: key combination not supported",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Erro: combinação de chaves não suportada",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #9

    params = [
        [['Text',], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The 'all' key cannot be used combined with other keys, but we got:",], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["A chave 'all' não pode ser combinada com outras chaves, mas obtivemos:",], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _check_which_density_gaussian_kernal_plot()
