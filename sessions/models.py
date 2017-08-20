""" SCHEMA
    create table sessions(
        session_key varchar(50),
        session_value varchar(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expiry_date datetime,
    );

"""


from constants import AppConstants
import MySQLdb
class SessionModel:

    def __init__(self):

        self.tableName = 'sessions'
        user = AppConstants.db_user 
        db_password = AppConstants.db_password
        db_name = AppConstants.db_name
        self.connection = MySQLdb.connect(user= user, passwd =db_password , db = db_name)
        self.cursor = self.connection.cursor()

    def get_by_key(self, key):
        sqlQuery = 'select * from sessions where session_key = %s' ;
        self.cursor.execute(sqlQuery, (key,))
        rows = self.cursor.fetchone()
        return rows 

    def insert_session(self, key, value):
        sqlQuery = "insert into sessions (`session_key`, `session_value`) values (%s, %s)" ;
        self.cursor.execute(sqlQuery, (key, value))
        self.connection.commit()