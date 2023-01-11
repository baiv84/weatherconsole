# -*- coding: utf-8 -*-
import requests


def extract_page(city):
    """Get HTML response from page"""
    # HTTP requests params
    params = {
        'nqmMT': '',
        'lang': 'ru',
    }

    # Generate link to get weather conditions over API service
    link = 'https://wttr.in/%s' % (city)

    # Download page content for particular city
    response = requests.get(link, params=params)
    if response.status_code != requests.codes.ok:
        page = None
    else:
        page = response.text

    return page
