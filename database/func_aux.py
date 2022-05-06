import sqlite3
from pathlib import Path

class Funcoes:

    def __init__(self):
        pass



    def query_func_id(nome, cursor, connection):
        """
        Retorna o id_funcao de uma função.
        nome é uma string com o nome da função desejada
        """

        cursor.execute("""
        SELECT
            id_funcao
        FROM
            Funcao
        WHERE
            nome = ?
        ;
        """, (nome,) )
        query = cursor.fetchone()
        return query


    def insert_into_message_message_parts(messages, position, fk_id_function, fk_id_language, cursor, connection, fk_id_contributor=1):
        """
        messages deve ser uma lista
        """
        # inserindo em Message
        cursor.execute("""
            INSERT INTO Message (position, fk_id_function, fk_id_language, fk_id_contributor) VALUES (?, ?, ?, ?);
        """, (position, fk_id_function, fk_id_language, fk_id_contributor))
        connection.commit()

        # fazendo uma query para obter o id que acabou de ser inserido
        cursor.execute("""
            SELECT id_message FROM Message WHERE position = ? AND fk_id_function = ? AND fk_id_language = ?
        """, (position, fk_id_function, fk_id_language))

        query = cursor.fetchone()

        # Fazendo um loop para inserir todos os valores de message em Message_Parts, com o fk_id_message que acabou de ser consultado
        for message in messages:
            cursor.execute("""
                INSERT INTO Message_Slices (message, fk_id_message) VALUES (?, ?);
            """, (message, query[0]))
            connection.commit()


    def insert_into_default_message_message_slices(messages, position, fk_id_default_values, fk_id_language, cursor, connection, fk_id_contributor=1):
        """
        messages deve ser uma lista
        """
        # inserindo em Default_Messages_Slices
        cursor.execute("""
            INSERT INTO Default_Messages (position, fk_id_default_values, fk_id_language, fk_id_contributor) VALUES (?, ?, ?, ?);
        """, (position, fk_id_default_values, fk_id_language, fk_id_contributor))
        connection.commit()

        # fazendo uma query para obter o id que acabou de ser inserido
        cursor.execute("""
            SELECT id_default_message FROM Default_Messages WHERE position = ? AND fk_id_default_values = ? AND fk_id_language = ?
        """, (position, fk_id_default_values, fk_id_language))

        query = cursor.fetchone()


        for message in messages:
            cursor.execute("""
                INSERT INTO Default_Messages_Slices (message_slice, fk_id_default_messages) VALUES (?, ?);
            """, (message, query[0]))
            connection.commit()
