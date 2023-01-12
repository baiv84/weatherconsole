# -*- coding: utf-8 -*-
from tools.extractor import extract_page
from tools.printer import print_page


# Internet links to weather resources
CITY_NAMES = [
    'лондон',
    'шереметьево',
    'череповец',
]

# Program entry point
if __name__ == '__main__':
    # Perform page extractions
    pages = [extract_page(city_name) for city_name in CITY_NAMES]

    # Print weather conditions  to Console
    for page in pages:
        print_page(page)
