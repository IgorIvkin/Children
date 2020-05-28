"""
Author: Igor
Date 2020.05.28
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, g


class DatabaseSetup(object):
    """This class is intended to setup database configuration and
    creates SQLAlchemy instances"""
    app: Flask = None
    config_url = ''
    database_engine = None

    def __init__(self, app):
        # Check if app is defined
        if app is None:
            raise ValueError('Cannot initialize database for an empty application')
        else:
            self.app = app

        # Check if configuration string is defined
        if app.config['SQLALCHEMY_DATABASE_URI'] == '':
            raise ValueError('You have to define SQLALCHEMY_DATABASE_URI parameter in ' +
                             'your config to initialize database')
        else:
            self.config_url = app.config['SQLALCHEMY_DATABASE_URI']

        # Now create the database engine and store it in the global context
        self.database_engine = SQLAlchemy(app)
        if self.database_engine is None:
            raise ValueError('Cannot initialize engine by an unknown reason. Database engine is None')
        g.database_engine = self.database_engine

    def get_db(self):
        """Returns currently initialized database engine"""
        return self.database_engine
