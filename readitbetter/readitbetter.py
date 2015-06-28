# -*- coding: utf-8 -*-
from lxml.html.clean import Cleaner


def clean_up_html(html):
    """
    Cleans up the HTML and strips away unwanted attributes
    :param html:
    :return:
    """
    html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
                           forms=True, annoying_tags=True, processing_instructions=True,
                           links=True)
    return html_cleaner.clean_html(html)
