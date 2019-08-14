#!/usr/bin/python3
'''DBStorage engine'''

import MySQLdb
import os

class DBStorage:
    '''class for DBStorage'''
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes DBStorage'''
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Query all objects on current database session'''
        if cls is None:




    def new(self, obj):
        '''Adds object to current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes of current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes obj from current database session'''
        if obj:
            self.__session.delete(obj)
            
    def reload(self):
        '''Creates current db session from engine and all tables in db'''
        Base.metadata.create_all(self.__engine)



