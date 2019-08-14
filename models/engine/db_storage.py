#!/usr/bin/python3
'''DBStorage engine'''

import MySQLdb
from models import City, State, Place, Review, Amenity, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
            # Drop all tables for testing purposes

    def all(self, cls=None):
        '''Query all objects on current database session'''
        all_dict = {}
        if cls:
            x = self.__session.query(cls).all()
        else:
            x = self.__session.query(User).all()
            x += self.__session.query(State).all()
            x += self.__session.query(City).all()
            x += self.__session.query(Amenity).all()
            x += self.__session.query(Place).all()
            x += self.__session.query(Review).all()

        for obj in x:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            # key convention - <class-name>.<object-id>
            all_dict[key] = obj
        return all_dict

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

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
