import re
from urllib.parse import urlparse

MOST_OFTEN = ('COM', 'NET', 'ORG', 'INT', 'EDU', 'GOV', 'MIL', 'ARPA',
              'INFO', 'BIZ', 'NAME', 'COOP', 'MUSEUM', 'AERO', 'PRO', 'БЕЛ', 'СРБ', 'МОН')


def domain_name(url):
    url_peace = urlparse(url)
    all_domain = url_peace[1].split('.')
    for domain in reversed(all_domain[:-1]):
        if domain.upper() not in MOST_OFTEN and len(domain) > 2:
            return domain
    return 'Err'


enters_url = input()
print(domain_name(enters_url))
