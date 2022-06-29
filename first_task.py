import re
from urllib.parse import urlparse
from urllib.request import urlopen

DOMAIN_BASE_URL = \
    'https://www.reg.ru/domain/new/zonepedia?_gl=1*scshaj*_' \
    'ga*NzcwNDQyMzU5LjE2NTQ2NjE4Nzk.*_ga_N9GCQPR82H*MTY1NjUwOTY5Ni4zLjAuMTY1NjUwOTY5Ni42MA..'


def take_all_top_domain():
    answer = urlopen(DOMAIN_BASE_URL)
    html = str(answer.read())
    all_domains = re.findall('href="/domain/new/[A-zА-я0-9.-]+/">', html)
    all_domains = list(map(lambda domain: domain[18:-3].lower(), all_domains))
    all_domains.sort(key=len)
    return all_domains


def domain_name(url):
    url_peace = str(urlparse(url)[1]).lower()
    all_domains = take_all_top_domain()
    for domain in reversed(all_domains):
        reg_string = '[.]{1}' + domain + '[.]?'
        check_include = re.findall(reg_string, url_peace)
        if check_include:
            position = url_peace.find(check_include[0])
            url_peace = url_peace[:position] + url_peace[position + len(domain) + 1:]
    return url_peace.split('.')[-1]


enters_url = input()
print(domain_name(enters_url))
