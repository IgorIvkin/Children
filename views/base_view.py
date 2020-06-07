"""
Author: Igor
Date: 2020.06.07
"""

from flask import render_template


class HTMLView(object):
    """Represents a base class to render a HTML-presentation.
    """
    def __init__(self, main_template):
        self.main_template = main_template
        self.header = ''
        self.footer = ''
        self.title = ''
        self.js = []

    def set_header(self, header):
        self.header = header
        return self

    def set_footer(self, footer):
        self.footer = footer
        return self

    def set_title(self, title):
        self.title = title
        return self

    def add_js(self, js_file_name):
        if js_file_name not in self.js:
            self.js.append(js_file_name)
        return self

    def render(self):
        return render_template(self.main_template,
                               header=self.header,
                               footer=self.footer,
                               title=self.title,
                               js=self.js)
