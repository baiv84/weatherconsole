# -*- coding: utf-8 -*-
import requests


def extract_page(city):
    """Get HTML response from page"""
    # HTTP requests params
    params = {
        'n': '',                        # Short output mode (only day/night)
        'q': '',                        # Silent mode
        'M': '',                        # Metric system
        'T': '',                        # Disable terminal escapes (no colour)
        '2': '',                        # Weather only for today + 1 day
        'lang': 'ru',                   # Language - russian
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
