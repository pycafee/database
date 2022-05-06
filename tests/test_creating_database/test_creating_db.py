"""Testing if the table "main_database.db" was created correctly

---> Class TestCheckFileExists

This class tests if the file "main_database.db" exists

-------------------------------


---> Class TestCheckTablesNames

This class tests if each of the 9 tables has been created. The names of the tables are:

    - Contributor;
    - Default_Messages_slices;
    - Default_Messages;
    - Default_Values;
    - Funcao;
    - Language;
    - Languages_Contributor;
    - Message;
    - Message_Slices;

There's one last test checking a table name that doesn't exist, but it's not useful

-------------------------------


---> Class TestCheckTablesColumnNames

This class tests if each table has all the expected columns. The name of each column for each table is:

    - Contributor:
        ['id_contributor', 'username', 'email', 'name', 'middle_name', 'last_name']
    - Default_Messages_slices:
        ['id_default_message', 'position', 'date', 'last_update', 'fk_id_default_values', 'fk_id_contributor', 'fk_id_language']
    - Default_Messages:
        ['id_default_message_slices', 'message_slice', 'fk_id_default_messages']
    - Default_Values:
        ['id_default_values', 'default_parameter', 'default_input']
    - Funcao:
        ['id_funcao', 'nome']
    - Language:
        ['id_language', 'language']
    - Languages_Contributor:
        ['id_tongue', 'fk_id_contributor', 'fk_id_language']
    - Message;
        ['id_message', 'position', 'date', 'last_update', 'fk_id_function', 'fk_id_contributor', 'fk_id_language']
    - Message_Slices:
    ['id_message_slice', 'message', 'fk_id_message']

-------------------------------


Command to run at the prompt:
    python -m unittest -v tests/test_creating_database/test_creating_db.py

-------------------------------


Author:
    Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

-------------------------------


Created:
    4th April, 2022.

"""


from pathlib import Path
import sqlite3
from database.func_aux import Funcoes as func
import unittest


class TestCheckFileExists(unittest.TestCase):

    def test_check_file_exits(self):
        database = Path("main_database.db")
        self.assertTrue(database.exists(), "The 'main_database.db' does not exists!")


class TestCheckTablesNames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name="main_database.db"
        data = Path(database_name)
        cls.connection = sqlite3.connect(database_name)
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.cursor.close()
        cls.connection.close()

    def test_query_table_Contributor(self):
        self.cursor.execute("""
            SELECT * FROM Contributor
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Contributor!")

    def test_query_table_Default_Messages(self):
        self.cursor.execute("""
            SELECT * FROM Default_Messages
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Default_Messages!")

    def test_query_table_Default_Messages_slices(self):
        self.cursor.execute("""
            SELECT * FROM Default_Messages_slices
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Default_Messages_slices!")

    def test_query_table_Default_Values(self):
        self.cursor.execute("""
            SELECT * FROM Default_Values
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Default_Values!")

    def test_query_table_Funcao(self):
        self.cursor.execute("""
            SELECT * FROM Funcao
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries inFuncao!")

    def test_query_table_Language(self):
        self.cursor.execute("""
            SELECT * FROM Language
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Language!")

    def test_query_table_Languages_Contributor(self):
        self.cursor.execute("""
            SELECT * FROM Languages_Contributor
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Languages_Contributor!")

    def test_query_table_Message(self):
        self.cursor.execute("""
            SELECT * FROM Message
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Message!")

    def test_query_table_Message_Slices(self):
        self.cursor.execute("""
            SELECT * FROM Message_Slices
        ;
        """)
        query = self.cursor.fetchone()
        self.assertIsNone(query, "There are entries in Message_Slices!")

    def test_query_table_XXX(self):
        with self.assertRaises(sqlite3.OperationalError, msg="There table XXX exits!"):
            self.cursor.execute("""
                SELECT * FROM XXX
            ;
            """)
            query = self.cursor.fetchone()


class TestCheckTablesColumnNames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name="main_database.db"
        data = Path(database_name)
        cls.connection = sqlite3.connect(database_name)
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.cursor.close()
        cls.connection.close()

    def test_query_table_Contributor(self):
        self.cursor.execute("""
            SELECT * FROM Contributor
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_contributor', 'username', 'email', 'name', 'middle_name', 'last_name']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Contributor' table!")

    def test_query_table_Default_Messages(self):
        self.cursor.execute("""
            SELECT * FROM Default_Messages
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_default_message', 'position', 'date', 'last_update', 'fk_id_default_values', 'fk_id_contributor', 'fk_id_language']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Default_Messages' table!")

    def test_query_table_Default_Messages_slices(self):
        self.cursor.execute("""
            SELECT * FROM Default_Messages_slices
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_default_message_slices', 'message_slice', 'fk_id_default_messages']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Default_Messages_slices' table!")

    def test_query_table_Default_Values(self):
        self.cursor.execute("""
            SELECT * FROM Default_Values
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_default_values', 'default_parameter', 'default_input']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Default_Values' table!")

    def test_query_table_Funcao(self):
        self.cursor.execute("""
            SELECT * FROM Funcao
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_funcao', 'nome']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Funcao' table!")

    def test_query_table_Language(self):
        self.cursor.execute("""
            SELECT * FROM Language
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_language', 'language']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Language' table!")

    def test_query_table_Languages_Contributor(self):
        self.cursor.execute("""
            SELECT * FROM Languages_Contributor
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_tongue', 'fk_id_contributor', 'fk_id_language']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Languages_Contributor' table!")

    def test_query_table_Message(self):
        self.cursor.execute("""
            SELECT * FROM Message
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_message', 'position', 'date', 'last_update', 'fk_id_function', 'fk_id_contributor', 'fk_id_language']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Message' table!")

    def test_query_table_Message_Slices(self):
        self.cursor.execute("""
            SELECT * FROM Message_Slices
        ;
        """)
        query = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        expected_column_names = ['id_message_slice', 'message', 'fk_id_message']
        self.assertCountEqual(expected_column_names, column_names, "Table columns are different than expected for 'Message_Slices' table!")

#


if __name__ == '__main__':
    unittest.main()

#
