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
    caption: Want to preserve tables
    cite: Not a nuisance.
    code: Want to preserve code snippets
    col: Want to preserve tables
    colgroup: Want to preserve tables
    dd: Might be useful
    del: Same as dd
    dfn: same as abbr
    div: Very widely used within content
    dl: same as dd
    dt: same as dd
    em: same as b
    embed: Want to retain embedded videos
    h1-h6: Want to retain headings
    header: same as h1-h6
    hr: Same as br
    i: Same as em
    iframe: same as embed
    img: want to retain images
    ins: Same as del
    li: Want to retain lists
    main: Might be useful
    mark: same as br
    ol: same as li
    p: Want to retain paragraphs
    pre: Want to retain code snippets
    q: Want to retain quotes
    section: Same as br
    small: same as br
    span: same as div
    strong: same as em
    summary: same as caption
    """
    tags_whitelist = ['a', 'abbr', 'article', 'b', 'base', 'bdi', 'bdo', 'blockquote', 'br', 'caption',
                      'cite', 'code', 'col', 'colgroup', 'dd', 'dfn', 'div', 'dl', 'dt', 'em',
                      'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'i', 'img', 'li', 'main',
                      'mark', 'ol', 'p', 'pre', 'q', 'section', 'small', 'div', 'strong', 'summary']
    embeds_whitelist = ['embed', 'iframe']
    # html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
    #                        forms=True, annoying_tags=True, processing_instructions=True,
    #                        links=True)
    return
