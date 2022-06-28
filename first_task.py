import re


def domain_name(url):
    all_regular = re.findall('[A-zА-я0-9.-]+', url)
    for example in all_regular:
        if example[-1] != '.' and example[0] != '.' and example.find('.') != -1:
            return example.split('.')[-2]
    return 'Err'


enters_url = input()

print(domain_name(enters_url))
