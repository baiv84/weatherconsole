# -*- coding: utf-8 -*-
from tools.extractor import extract_page
from tools.printer import print_page


# Internet links to weather resources
CITIES = [
    'лондон',
    'шереметьево',
    'череповец',
]

# Program entry point
if __name__ == '__main__':
    # Perform page extractions
    pages = [extract_page(city) for city in CITIES]

    # Print weather conditions  to Console
    for page in pages:
        print_page(page)
