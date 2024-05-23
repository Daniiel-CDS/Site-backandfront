from peewee import MySQLDatabase
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_NAME = getenv('DB_USER')
DB_HOST = getenv('DB_HOST')
DB_DATABASE = getenv('DB_DATABASE')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_PORT = getenv('DB_PORT')


db = MySQLDatabase(DB_DATABASE, user=DB_NAME, password=DB_PASSWORD,
                         host=DB_HOST, port=int(DB_PORT))
