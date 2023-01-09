# -*- coding: utf-8 -*-
import requests


def extract_page(city):
    """Get HTML response from page"""

    # Generate link to get weather conditions over API service
    link = 'https://wttr.in/%s?nqmMT&lang=ru' % (city)

    # Download page content for particular city
    try:
        response = requests.get(link)
        page = response.text
    except ConnectionError:
        page = None

    return page
