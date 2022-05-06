import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def insert_default_inserts(database_name="base.db"):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()


    ###########################################
    ############ Default Language #############
    ###########################################

    ###########################################
    position = 1
    fk_id_default_values = 1 # langauge default parameter
    fk_id_contributor = 1

    params = [
        [["Text", "$Parameter$",  "Text", "$Text$",  "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The '", "$Parameter$", "' parameter only accepts string variables, but we got '", "$Text$", "'"], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["O parâmetro '", "$Parameter$",  "' aceita apenas variaveis do tipo string, mas obtivemos '", "$Text$",  "'"], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text", "$Text$", "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The desired language ('", "$Text$", "') is already the default language."], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma desejado ('", "$new_language$", "') já é o idioma padrão."], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text", "$Text$", "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The desired language ('", "$Text$", "') is not available."], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma desejado ('", "$Text$", "') não esta disponível."], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################

    ###########################################
    position = position + 1

    params = [
        [["Text",], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The languages available are:",], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Os idiomas disponíveis são:",], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text",], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["WARNING: you are about to change a default value for the entire library! Proceed carefully!!!",], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["AVISO: você está prestes a alterar um valor padrão para toda a biblioteca! Prossiga com cuidado!!!",], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text",], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["Press enter to continue",], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Pressione enter para continuar",], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text",], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["This is a highly sensitive change and there is no guarantee that 100% of all texts will be changed to the new language!",], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Esta é uma alteração altamente sensível e não há garantia de que 100% de todos os textos serão alterados para o novo idioma!",], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text", "$Text$", "Text", "$Text$", "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["Are you sure you want to change the language from '", "$Text$", "' to '", "$Text$", "'?    Y / n    "], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Você tem certeza que deseja alterar o idioma de '", "$Text$", "' para '", "$Text$", "'?    Y / n    "], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text",], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["User response: ",], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Resposta do usuário: ",], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text", "$Text$", "Text", "$Text$", "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The default language has been changed from '", "$Text$", "' to '", "$Text$",  "' successfully!"], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma padrão foi alterado de '", "$Text$", "' para '", "$Text$", "' com sucesso!"], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["Procedure aborted by user."], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["Procedimento abortado pelo usuário."], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    ###########################################
    position = position + 1

    params = [
        [["Text", "$Text$", "Text"], position, fk_id_default_values, 1, cursor, connection, fk_id_contributor], # univ
        [["The default language has not been changed, and remains '", "$Text$", "'."], position, fk_id_default_values, 2, cursor, connection, fk_id_contributor], # en
        [["O idioma padrão não foi alterado, e permanece '", "$Text$", "'."], position, fk_id_default_values, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_default_message_message_slices(*param)
    ###########################################

    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()



if __name__ == '__main__':
    insert_default_inserts()
