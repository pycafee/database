"""Creates the database

A module with "creating_databse" as main function, which has all the DDL comands.

Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: 4th April, 2022.

"""

import sqlite3
from pathlib import Path


def creating_database(database_name):

    data = Path(database_name)

    if data.exists():
        data.unlink()
    else:
        pass

    ################################################################
    ####################   CRIANDO A DATABASE   ####################
    ################################################################

    connection = sqlite3.connect(database_name)

    cursor = connection.cursor()

    #################################
    ### CRIANDO A TABELA LANGUAGE ###
    #################################

    cursor.execute("""
    CREATE TABLE Language (
        id_language INTEGER PRIMARY KEY AUTOINCREMENT,
        language VARCHAR (5) UNIQUE NOT NULL CHECK (LENGTH(language) <=5)
    );
    """)
    connection.commit()


    ###############################
    ### CRIANDO A TABELA FUNCAO ###
    ###############################

    cursor.execute("""
    CREATE TABLE Funcao (
        id_funcao INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(51) NOT NULL UNIQUE CHECK (LENGTH(nome) <=51)
    );
    """)
    connection.commit()


    ####################################
    ### CRIANDO A TABELA CONTRIBUTOR ###
    ####################################

    cursor.execute("""
    CREATE TABLE Contributor (
        id_contributor INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(15) NOT NULL UNIQUE CHECK (LENGTH(username) <=15),
        email VARCHAR(51) NOT NULL UNIQUE CHECK (LENGTH(email) <=51),
        name VARCHAR(15) NOT NULL CHECK (LENGTH(name) <=15),
        middle_name VARCHAR(51) CHECK (LENGTH(middle_name) <=51),
        last_name VARCHAR(15) NOT NULL CHECK (LENGTH(last_name) <=15),
        UNIQUE (
            email,
            username
          )
    );
    """)
    connection.commit()


    ##############################################
    ### CRIANDO A TABELA LANGUAGES_CONTRIBUTOR ###
    ##############################################

    cursor.execute("""
    CREATE TABLE Languages_Contributor (
        id_tongue INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_id_contributor INTEGER NOT NULL,
        fk_id_language INTEGER NOT NULL REFERENCES Language (id_language),
        UNIQUE (
            fk_id_contributor,
            fk_id_language
        )
        ON CONFLICT ABORT
    );
    """)
    connection.commit()


    ################################
    ### CRIANDO A TABELA MESSAGE ###
    ################################

    cursor.execute("""
    CREATE TABLE Message (
        id_message INTEGER PRIMARY KEY AUTOINCREMENT,
        position INTEGER NOT NULL,
        date DATETIME NOT NULL DEFAULT CURRENT_DATE,
        last_update DATETIME,
        fk_id_function INTEGER NOT NULL REFERENCES Funcao (id_funcao),
        fk_id_contributor INTEGER NOT NULL REFERENCES Contributor (id_contributor),
        fk_id_language INTEGER NOT NULL REFERENCES Language (id_language),
        UNIQUE (
            fk_id_function,
            position,
            fk_id_language
        )
        ON CONFLICT ABORT
    );
    """)
    connection.commit()


    ######################################
    ### CRIANDO A TABELA Message_Parts ###
    ######################################

    cursor.execute("""
    CREATE TABLE Message_Slices (
        id_message_slice INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL,
        fk_id_message INTEGER NOT NULL REFERENCES Message (id_message)
    );
    """)
    connection.commit()

    #######################################
    ### CRIANDO A TABELA Default_Values ###
    #######################################

    cursor.execute("""
    CREATE TABLE Default_Values (
        id_default_values INTEGER PRIMARY KEY AUTOINCREMENT,
        default_parameter VARCHAR(20) NOT NULL UNIQUE CHECK (LENGTH(default_parameter) <=20),
        default_input VARCHAR(20) NOT NULL UNIQUE CHECK (LENGTH(default_input) <=20),
        UNIQUE (
            default_parameter,
            default_input
          )
    );
    """)
    connection.commit()

    #########################################
    ### CRIANDO A TABELA Default_Messages ###
    #########################################

    cursor.execute("""
    CREATE TABLE Default_Messages (
        id_default_message INTEGER PRIMARY KEY AUTOINCREMENT,
        position INTEGER NOT NULL,
        date DATETIME NOT NULL DEFAULT CURRENT_DATE,
        last_update DATETIME,
        fk_id_default_values INTEGER NOT NULL REFERENCES Funcao (id_default_values),
        fk_id_contributor INTEGER NOT NULL REFERENCES Contributor (id_contributor),
        fk_id_language INTEGER NOT NULL REFERENCES Language (id_language),
        UNIQUE (
            fk_id_default_values,
            position,
            fk_id_language
        )
        ON CONFLICT ABORT
    );
    """)
    connection.commit()


    ################################################
    ### CRIANDO A TABELA Default_Messages_Slices ###
    ################################################

    cursor.execute("""
    CREATE TABLE Default_Messages_Slices (
        id_default_message_slices INTEGER PRIMARY KEY AUTOINCREMENT,
        message_slice TEXT NOT NULL,
        fk_id_default_messages INTEGER NOT NULL REFERENCES Default_Messages (id_default_messages)
    );
    """)
    connection.commit()


    #################################################################
    ####################   FECHANDO A DATABASE   ####################
    #################################################################


    cursor.close()
    connection.close()


if __name__ == '__main__':
    creating_database()
