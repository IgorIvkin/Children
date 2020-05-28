"""
Author: Igor
Date: 2020.05.28
"""

from flask import g
from flask_sqlalchemy import SQLAlchemy


def get_database_engine():
    db: SQLAlchemy = g.database_engine
    return db
