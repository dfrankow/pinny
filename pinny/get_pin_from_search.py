#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

# default 'not found' pin
_NOT_FOUND_HREF = "https://pinterest.com/pin/518547344579159344/"
_NOT_FOUND_IMG_SRC = 'https://s-media-cache-ak0.pinimg.com/originals/34/39/86/3439860e1ff8ae02529cb9cce01827c4.png'


def get_page_text(query):
    """Get a page of text from Pinterest search."""
    result = requests.get('https://www.pinterest.com/search/pins/?q=%s' % query)
    page_text = ''
    if result:
        page_text = result.text
    return page_text


def get_first_pin_from_search_result(query):
    """Return first pin from search results.

    Returns a tuple: ('/pin/the_id', 'link-to-image')
    """
    if query:
        page_text = get_page_text(query)
        return _parse_first_pin_from_search_result(page_text)
    else:
        return (_NOT_FOUND_HREF, _NOT_FOUND_IMG_SRC)


def _parse_first_pin_from_search_result(page_text):
    """Return first pin from search results.

    Returns a tuple: ('/pin/the_id', 'link-to-image')
    """
    # pull out the first pin result
    soup = BeautifulSoup(page_text, 'html.parser')
    # default 'not found' pin
    href = _NOT_FOUND_HREF
    img_src = _NOT_FOUND_IMG_SRC
    pinwrapper = soup.find("a", "pinImageWrapper")
    if pinwrapper:
        href = "https://pinterest.com%s" % pinwrapper.get('href')
        img_src = pinwrapper.img.get('src')
    return (href, img_src)

def main(args):

    print "%s %s" % the_tuple
