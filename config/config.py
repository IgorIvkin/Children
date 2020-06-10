"""
Author: Igor
Date: 2020.05.22
"""


class BaseConfiguration(object):
    """This class represents basic configuration of the application, it uses default database.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'some_secret_key_here!@y12o31op2jh'
    SQLALCHEMY_DATABASE_URI = 'postgresql://children:children556677@localhost/childrenmain'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://children:children556677@localhost/childrentest'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfiguration(BaseConfiguration):
    """This class represents a testing environment of the application, it points to the test database
    instead of common database and activates testing.
    """
    Debug = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://children:children556677@localhost/childrentest'
    SQLALCHEMY_ECHO = True
