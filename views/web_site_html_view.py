"""
Author: Igor
Date: 2020.06.11
"""

from views.html_view import HtmlView


class WebSiteHtmlView(HtmlView):
    """
    It is basic admin HtmlView, it mostly exists to encapsulate
    default header and footer for most part of admin pages.
    """
    def __init__(self, main_template):
        super().__init__(main_template)
        self.header = 'main_blocks/main_header.html'
        self.footer = 'main_blocks/main_footer.html'
