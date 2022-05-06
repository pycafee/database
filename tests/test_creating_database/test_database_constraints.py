"""Testing if the constraints applied on the "main_database.db" are correct

---> TestCheckContributorConstraints
    This class tests if thethe constraints of the "Contributor" table are correct

---> Class TestCheckLanguageConstraints
    This class tests if the the constraints of the "Language" table are correct

---> Class TestCheckFuncaoConstraints
    This class tests if the constraints of the "Funcao" table are correct

---> Class TestCheckDefault_ValuesConstraints
    This class tests if the constraints of the "Default_Values" table are correct

--------------------------------------------------------------------------------

Command to run at the prompt:
    python -m unittest -v tests/test_creating_database/test_database_constraints.py

--------------------------------------------------------------------------------


Author:
    Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

--------------------------------------------------------------------------------


Created:
    14th April, 2022.


--------------------------------------------------------------------------------
"""




from pathlib import Path
import sqlite3
from database.func_aux import Funcoes as func
import unittest


### Precisa criarfunções decentes para funcionar direito
class TestCheckMessageConstraints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name = "main_database.db"
        source = sqlite3.connect(database_name)
        cls.memory_connection = sqlite3.connect(':memory:')
        source.backup(cls.memory_connection)
        cls.cursor = cls.memory_connection.cursor()
        source.close()

        ### Criando a database fake ###
        ## inserindo um Contributor ##
        cls.cursor.executemany("""
            INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
        """, [('aiolia22','andersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
        cls.memory_connection.commit()

        cls.cursor.execute("""SELECT id_contributor FROM Contributor WHERE username = 'aiolia22';
        """)
        cls.fk_id_contributor = cls.cursor.fetchone()[0]

        ## inserindo uma funcao ##
        cls.cursor.executemany("""
            INSERT INTO Funcao VALUES (NULL, ?);
        """, [('shapiro_wilk',)])
        cls.memory_connection.commit()

        cls.cursor.execute("""SELECT id_funcao FROM Funcao WHERE nome = 'shapiro_wilk';
        """)
        cls.fk_id_function = cls.cursor.fetchone()[0]

        ## inserindo um idioma ##
        cls.cursor.executemany("""
            INSERT INTO Language VALUES (NULL, ?);
        """, [('en',)])
        cls.memory_connection.commit()

        cls.cursor.execute("""SELECT id_language FROM Language WHERE language = 'en';
        """)
        cls.fk_id_language = cls.cursor.fetchone()[0]

        cls.position = 1

        # inserindo um Message
        cls.cursor.execute("""
            INSERT INTO Message (position, fk_id_function, fk_id_language, fk_id_contributor) VALUES (?, ?, ?, ?);
        """, (cls.position, cls.fk_id_function, cls.fk_id_language, cls.fk_id_contributor))
        cls.memory_connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.memory_connection.close()

    ### Column data ###
    # data must be NOT NULL
    def test_constraint_not_null_data(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'data' in 'Message' failed"):
            self.cursor.execute("""
                INSERT INTO Message (position, date, fk_id_function, fk_id_language, fk_id_contributor) VALUES (?, ?, ?, ?, ?);
            """, (2, None, self.fk_id_function, self.fk_id_language, self.fk_id_contributor))
            self.memory_connection.commit()


    # last_updata can be null
    def test_constraint_null_last_update(self):
        teste = False
        try:
            self.cursor.execute("""
                INSERT INTO Message (position, last_update, fk_id_function, fk_id_language, fk_id_contributor) VALUES (?, ?, ?, ?, ?);
            """, (2, None, self.fk_id_function, self.fk_id_language, self.fk_id_contributor))
            self.memory_connection.commit()
            teste = True
        except sqlite3.IntegrityError:
            teste = False
        self.assertTrue(teste, msg="Unable to insert a NULL value in the column 'last_update' of the 'Message' table")






class TestCheckDefault_ValuesConstraints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name = "main_database.db"
        source = sqlite3.connect(database_name)
        cls.memory_connection = sqlite3.connect(':memory:')
        source.backup(cls.memory_connection)
        cls.cursor = cls.memory_connection.cursor()
        source.close()

        # inserindo um Default_Values
        cls.cursor.executemany("""
            INSERT INTO Default_Values VALUES (NULL, ?, ?);
        """, [('language', 'en'),])
        cls.memory_connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.memory_connection.close()

    ### Column default_input ###
    # default_input length must be less then 20
    def test_constraint_varchar_20_default_input(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=20 constraint applied on the column 'default_input' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [('peteca', 'l'*21),])
            self.memory_connection.commit()

    # default_input must be not null
    def test_constraint_not_null_default_input(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'default_input' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [('peteca', None),])
            self.memory_connection.commit()

    # default_input must be unique
    def test_constraint_unique_default_input(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'default_input' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [('peteca', 'en'),])
            self.memory_connection.commit()

    ### Column default_parameter ###
    # default_parameter length must be less then 20
    def test_constraint_varchar_20_default_parameter(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=20 constraint applied on the column 'default_parameter' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [('l'*21, 'pt-br'),])
            self.memory_connection.commit()

    # default_parameter must be not null
    def test_constraint_not_null_default_parameter(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'default_parameter' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [(None, 'pt-br'),])
            self.memory_connection.commit()

    # default_parameter must be unique
    def test_constraint_unique_default_parameter(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'default_parameter' in 'Default_Values' failed"):
            self.cursor.executemany("""
                INSERT INTO Default_Values VALUES (NULL, ?, ?);
            """, [('language', 'pt-br'),])
            self.memory_connection.commit()

    ### Default_Values ###
    # the table has some value
    def test_Default_Values(self):
        self.cursor.execute("""SELECT * FROM Default_Values;""")
        query = self.cursor.fetchone()
        self.assertIsInstance(query, tuple, "There is no entry in 'Default_Values' table")

class TestCheckFuncaoConstraints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name = "main_database.db"
        source = sqlite3.connect(database_name)
        cls.memory_connection = sqlite3.connect(':memory:')
        source.backup(cls.memory_connection)
        cls.cursor = cls.memory_connection.cursor()
        source.close()

        # inserindo uma funcao
        cls.cursor.executemany("""
            INSERT INTO Funcao VALUES (NULL, ?);
        """, [('shapiro_wilk',)])
        cls.memory_connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.memory_connection.close()

    ### Column nome ###
    # nome length must be less then 52
    def test_constraint_varchar_51_nome(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=51 constraint applied on the column 'nome' in 'Funcao' failed"):
            self.cursor.executemany("""
                INSERT INTO Funcao VALUES (NULL, ?);
            """, [('shapiro_wilkshapiro_wilkshapiro_wilkshapiro_wilkshapiro_wilk',)])
            self.memory_connection.commit()

    # nome must be not null
    def test_constraint_not_null_nome(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'nome' in 'Funcao' failed"):
            self.cursor.executemany("""
                INSERT INTO Funcao VALUES (NULL, ?);
            """, [(None,)])
            self.memory_connection.commit()

    # nome must be unique
    def test_constraint_unique_nome(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'nome' in 'Funcao' failed"):
            self.cursor.executemany("""
                INSERT INTO Funcao VALUES (NULL, ?);
            """, [('shapiro_wilk',)])
            self.memory_connection.commit()

    ### Funcao ###
    # the table has some value
    def test_Language(self):
        self.cursor.execute("""SELECT * FROM Funcao;""")
        query = self.cursor.fetchone()
        self.assertIsInstance(query, tuple, "There is no entry in 'Funcao' table")

class TestCheckLanguageConstraints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name = "main_database.db"
        source = sqlite3.connect(database_name)
        cls.memory_connection = sqlite3.connect(':memory:')
        source.backup(cls.memory_connection)
        cls.cursor = cls.memory_connection.cursor()
        source.close()

        # inserindo um idioma
        cls.cursor.executemany("""
            INSERT INTO Language VALUES (NULL, ?);
        """, [('en',)])
        cls.memory_connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.memory_connection.close()

    ### Column language ###
    # language length must be less then 6
    def test_constraint_varchar_5_language(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=5 constraint applied on the column 'language' in 'Language' failed"):
            self.cursor.executemany("""
                INSERT INTO Language VALUES (NULL, ?);
            """, [('ennnnn',)])
            self.memory_connection.commit()

    # language must be not null
    def test_constraint_not_null_language(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'language' in 'Language' failed"):
            self.cursor.executemany("""
                INSERT INTO Language VALUES (NULL, ?);
            """, [(None,)])
            self.memory_connection.commit()

    # language must be unique
    def test_constraint_unique_language(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'language' in 'Language' failed"):
            self.cursor.executemany("""
                INSERT INTO Language VALUES (NULL, ?);
            """, [('en',)])
            self.memory_connection.commit()

    ### Language ###
    # the table has some value
    def test_Language(self):
        self.cursor.execute("""SELECT * FROM Language;""")
        query = self.cursor.fetchone()
        self.assertIsInstance(query, tuple, "There is no entry in 'Language' table")

class TestCheckContributorConstraints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        database_name = "main_database.db"
        source = sqlite3.connect(database_name)
        cls.memory_connection = sqlite3.connect(':memory:')
        source.backup(cls.memory_connection)
        cls.cursor = cls.memory_connection.cursor()
        source.close()

        # inserindo um Contributor
        cls.cursor.executemany("""
            INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
        """, [('aiolia22','andersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
        cls.memory_connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.memory_connection.close()

    ### Column middle_name ###
    # middle_name length must be less then 52
    def test_constraint_varchar_51_middle_name(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=51 constraint applied on the column 'middle_name' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', 'Anderson', 'Marcos Dias Marcos Dias Marcos Dias Marcos Dias Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # middle_name can be null
    def test_constraint_null_middle_name(self):
        teste = False
        try:
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', "Anderson", None, 'Canteli')])
            self.memory_connection.commit()
            teste = True
        except sqlite3.IntegrityError:
            teste = False
        self.assertTrue(teste, msg="Unable to insert a NULL value in the column 'middle_name' of the 'Contributor' table")

    ### Column name ###
    # name length must be less then 16
    def test_constraint_varchar_15_name(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=15 constraint applied on the column 'name' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', 'AndersonAnderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # name must not null
    def test_constraint_not_null_name(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'name' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', None, 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    ### Column last_name ###
    # last_name length must be less then 16
    def test_constraint_varchar_15_last_name(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=15 constraint applied on the column 'last_name' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', 'Anderson', 'Marcos Dias', 'CanteliCanteliCanteli')])
            self.memory_connection.commit()

    # last_name must not null
    def test_constraint_not_null_last_name(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'last_name' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','new_mail@gmail.com', "Anderson", 'Marcos Dias', None)])
            self.memory_connection.commit()

    ### Column email ###
    # email must be unique
    def test_constraint_unique_email(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'email' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','andersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # email must not null
    def test_constraint_not_null_email(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'email' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna', None, 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # email length must be less then 52
    def test_constraint_varchar_51_email(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=51 constraint applied on the column 'email' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('nosredna','andersonmdcanteliandersonmdcanteliandersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    ### Column username ###
    # username must be unique
    def test_constraint_unique_username(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The UNIQUE constraint applied on the column 'username' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('aiolia22','new_mail@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # username must not null
    def test_constraint_not_null_username(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The NOT NULL constraint applied on the column 'username' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [(None,'andersonmdcanteli@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    # username length must be less then 16
    def test_constraint_varchar_15_username(self):
        with self.assertRaises(sqlite3.IntegrityError, msg="The CHECK LENGTH <=15 constraint applied on the column 'username' in 'Contributor' failed"):
            self.cursor.executemany("""
                INSERT INTO Contributor VALUES (NULL, ?, ?, ?, ?, ?);
            """, [('aioliaaioliaaiolia','new_mail@gmail.com', 'Anderson', 'Marcos Dias', 'Canteli')])
            self.memory_connection.commit()

    ### fulltable ###
    # the table has some value
    def test_Contributor(self):
        self.cursor.execute("""SELECT * FROM Contributor;""")
        query = self.cursor.fetchone()
        self.assertIsInstance(query, tuple, "There is no entry in 'Contributor' table")















if __name__ == '__main__':
    unittest.main()
