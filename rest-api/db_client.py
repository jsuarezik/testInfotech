import os
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = 'localhost'
RDB_PORT = 28015
PROJECT_DB = 'test'
PROJECT_TABLE = 'users'

db_connection = r.connect(RDB_HOST, RDB_PORT)

def dbSetup():
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print 'Database setup completed.'
    except RqlRuntimeError:
        try:
            r.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print 'Table creation completed'
        except:
            print 'Table already exists.Nothing to do'

dbSetup()