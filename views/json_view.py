"""
Author: Igor
Date: 2020.06.08
"""

from flask import jsonify


class ErrorResponse(object):
    """This object represents a generic data about some error case.
    It includes string error_message, integer error_code and arbitrary
    dictionary of any data that could be related to error.
    """
    def __init__(self, error_message, error_code=-1, error_data=None):
        self.error_message = error_message
        self.error_code = error_code
        self.error_data = error_data


class BasicJsonView(object):
    """Basic object to represent json view.
    """
    pass


class JsonView(BasicJsonView):
    """Basic object to represent good json view.
    """
    @classmethod
    def render(cls, data_to_return):
        return jsonify({'status': 'ok',
                        'payload': data_to_return})


class ErrorJsonView(BasicJsonView):
    """Basic object to represent error json view.
    """
    @classmethod
    def render(cls, error: ErrorResponse):
        return jsonify({'status': 'error',
                        'payload': error})

