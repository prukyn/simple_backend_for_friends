
USER = 'here your username for owner a database'
PASSWORD = 'here your password for user'
DBNAME = 'here your database name'
HOST = 'localhost' # if you have host somewhere else, type here that host
PORT = 5432 # and port

# QUERIES
# INSIDE TRIPLE QUOTES WRITE YOUR QUERIES
HEADERS1 = []
QUERY1 = """  """

HEADERS2 = []
QUERY2 = """  """

HEADERS3 = []
QUERY3 = """  """

HEADERS4 = []
QUERY4 = """  """



# FLASK_SETTINGS
SECRET_KEY = 'SBVJHRBKVR131ASas'
DEBUG = False

try:
    from local_config import *
except ImportError:
    pass