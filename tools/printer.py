# -*- coding: utf-8 -*-
from tools.customexception import WeatherException


def print_page(page, method='echo'):
    """Print page content to the console.
       By default - just echo printing, without any changes
    """
    if method == 'echo' and page is not None:
        print(page)
    else:
        raise WeatherException('We have weather download exception')
