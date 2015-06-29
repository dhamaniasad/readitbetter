# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import bleach

def clean_up_html(html):
    """
    Cleans up the HTML and strips away unwanted attributes
    :param html:
    :return:
    """
    #  Tags list from http://html5doctor.com/element-index/
    """
    Why a specific tag is allowed
    a: We do not want to remove links from the document
    abbr: It isn't a nuisance tag and might contain useful information
    article: It will contain only information that's useful to us. If only everyone used it.
    b: This stylistic element is usually contained within the article
    base: Don't want broken relative urls
    bdi: Internationalization purposes
    bdo: Internationalization purposes
    blockquote: Not a nuisance.
    br: Useful formatting information
    """
    tags_whitelist = ['a', 'abbr', 'article', 'b', 'base', 'bdi', 'bdo', 'blockquote', 'br']
    # html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
    #                        forms=True, annoying_tags=True, processing_instructions=True,
    #                        links=True)
    return
