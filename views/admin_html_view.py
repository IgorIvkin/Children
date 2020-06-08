"""
Author: Igor
Date: 2020.06.08
"""

from views.html_view import HtmlView


class AdminHtmlView(HtmlView):
    """
    It is basic admin HtmlView, it mostly exists to encapsulate
    default header and footer for most part of admin pages.
    """
    def __init__(self, main_template):
        super().__init__(main_template)
        self.header = 'admin/main_blocks/main_header.html'
        self.footer = 'admin/main_blocks/main_footer.html'
