import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _export_to_csv(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_export_to_csv'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    #########################################
    ############ _export_to_csv #############
    #########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [['Text', "{file}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["UserWarning: The", "{file}", "already exists in the current folder."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["UserWarning: O arquivo", "{file}", "já existe no diretório atual"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [['Text', "{file_name}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The file will be exported with the name", "{file_name}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O arquivo será exportado com o nome ", "{file_name}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{file_name}", "file was exported!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O arquivo", "{file_name}", " foi exportado!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["You are not current allowed to change the", "{file_name}", "file"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Você não tem permissão para alterar o arquivo", "{file_name}", ""], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Hint ---> Maybe the", "{file_name}", "file is open! Please close the file and try again!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Dica ---> Talvez o arquivo", "{file_name}", "esta aberto! Por favor, feche-o e tente novamente!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Hint ---> If you are creating a file in a subfolder, create the folder in advance!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Dica ---> Se você esta criando o arquivo em uma subpasta, crie a pasta antes!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
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
    _export_to_csv()
