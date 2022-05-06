import sqlite3
from pathlib import Path
from database.func_aux import Funcoes as func

def _export_to_excel(database_name):


    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #############################################
    ############ INSERINDO EM FUNCAO ############
    #############################################

    func_name = '_export_to_excel'
    params = [
        (func_name,),
    ]
    cursor.executemany("""
        INSERT INTO Funcao VALUES (NULL, ?);
    """, params)

    connection.commit()

    ###########################################
    ############ _export_to_excel #############
    ###########################################

    id_funcao = func.query_func_id(func_name, cursor, connection)

    position = 1
    fk_id_function = id_funcao[0]
    fk_id_contributor = 1

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The", "{file_name}", "file contains sheets with the following names:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["O arquivo", "{file_name}", "contém abas com os seguintes nomes:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #2

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["And it was requested to save the data on the following tabs:"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["E foi solicitado para salvar os dados nas seguintes abas:"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #3

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["In order to avoid information loss, new names will be used for the sheets with conflicting sheet name."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Para evitar a perda de informação, novos nomes serão utilzados para as planilhas com nomes conflitantes"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #4

    params = [
        [["Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["No changes will be made to the data contained in these worksheets."], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["As planilhas originais não serão alteradas."], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #5

    params = [
        [["Text", "{file_name}"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["The data has been exported to file", "{file_name}"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Os dados foram exportados para o arquivo", "{file_name}"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #6

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["You are not current allowed to change the", "{file_name}", "file"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Você não tem permissão para alterar o arquivo", "{file_name}", ""], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #7

    params = [
        [["Text", "{file_name}", "Text"], position, fk_id_function, 1, cursor, connection, fk_id_contributor], # univ
        [["Hint ---> Maybe the", "{file_name}", "file is open! Please close the file and try again!"], position, fk_id_function, 2, cursor, connection, fk_id_contributor], # en
        [["Dica ---> Talvez o arquivo", "{file_name}", "esta aberto! Por favor, feche-o e tente novamente!"], position, fk_id_function, 3, cursor, connection, fk_id_contributor], # pt-br
    ]
    for param in params:
        func.insert_into_message_message_parts(*param)
    ###########################

    ###########################
    position = position + 1 #8

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
    _export_to_excel()
