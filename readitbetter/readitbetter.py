# -*- coding: utf-8 -*-
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup


def clean_up_html(html):
    """
    Cleans up the HTML and strips away unwanted attributes
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, parser='html5lib')
    remove_script_tags(soup)
    remove_form_tags(soup)
    remove_annoying_tags(soup)
    # html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
    #                        forms=True, annoying_tags=True, processing_instructions=True,
    #                        links=True)
    return soup


def remove_script_tags(soup):
    """
    Removes all script tags from the source
    :param soup:
    :return:
    """
    for tag in soup.find_all('script'):
        tag.extract()


def remove_form_tags(soup):
    """
    Removes all forms from the source
    :param soup:
    :return:
    """
    for tag in soup.find_all('form'):
        tag.extract()


def remove_annoying_tags(soup):
    """
    Removes annoying tags like blink and marquee
    :param soup:
    :return:
    """
    for tag in soup.find_all('blink'):
        tag.extract()
    for tag in soup.find_all('marquee'):
        tag.extract()