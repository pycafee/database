import sqlite3
from pathlib import Path


data = Path(database_name)
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
