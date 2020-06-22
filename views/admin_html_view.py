"""
Author: Igor
Date: 2020.06.08
"""

from views.html_view import HtmlView
from flask import render_template


class AdminHtmlView(HtmlView):
    """
    It is basic admin HtmlView, it mostly exists to encapsulate
    default header and footer for most part of admin pages.
    """
    def __init__(self, main_template):
        super().__init__(main_template)
        self.header = 'admin/main_blocks/main_header.html'
        self.footer = 'admin/main_blocks/main_footer.html'
        self.admin_menu = 'admin/main_blocks/menu.html'

    def set_admin_menu(self, admin_menu):
        self.admin_menu = admin_menu
        return self

    def render(self, **kwargs):
        return render_template(self.main_template,
                               header=self.header,
                               content=self.content,
                               footer=self.footer,
                               title=self.title,
                               js=self.js,
                               admin_menu=self.admin_menu,
                               **kwargs)
