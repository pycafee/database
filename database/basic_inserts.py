import sqlite3
from pathlib import Path


def basic_inserts(database_name='base.db'):

    ####################################################################
    ####################   CONECTANDO NA DATABASE   ####################
    ####################################################################

    data = Path(database_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    #################################################################
    ####################   FAZENDO INSERTS BASE   ####################
    ##################################################################


    ###############################################
    ############ INSERINDO EM LANGUAGE ############
    ###############################################

    cursor.executemany("INSERT INTO Language VALUES (NULL, ?);", [('univ',), ('en',), ('pt-br',)])
    connection.commit()

    ##################################################
    ############ INSERINDO EM CONTRIBUTOR ############
    ##################################################

    cursor.executemany("""
        INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
    """, [('aiolia22','andersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])

    connection.commit()

    ############################################################
    ############ INSERINDO EM LANGUAGES_CONTRIBUTOR ############
    ###########################################################

    cursor.executemany("""
        INSERT INTO Languages_Contributor VALUES (NULL, ?, ?);
    """, [(1,1), (1,2)]) # o id é o meu, e inserindo en e pt-br

    connection.commit()

    #####################################################
    ############ INSERINDO EM Default_Values ############
    #####################################################

    params = [
        ('language', 'en'),
    ]
    cursor.executemany("""
        INSERT INTO Default_Values VALUES (NULL, ?, ?);
    """, params)

    connection.commit()

    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################

    cursor.close()
    connection.close()


if __name__ == '__main__':
    basic_inserts()
