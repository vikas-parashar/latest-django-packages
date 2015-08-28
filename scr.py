# -- coding: utf-8 --
from bs4 import BeautifulSoup
import re
import requests
import urllib3

soup = BeautifulSoup(open("pypi.html"), "html.parser")

old = 'old.txt'
new = 'new.txt'
package_url_list = []
mail_content_list = []

def difference():
    with open(old) as f:
        t1 = f.read().splitlines()
        t1s = set(t1)

    with open(new) as f:
        t2 = f.read().splitlines()
        t2s = set(t2)

    diff_list = []
    for diff in t2s-t1s:
        diff_list.append(diff)
    return diff_list


def package_finder():
    thefile = open(new, 'w')
    for row in soup.find_all('a'):
        package_name = row.text
        pattern = 'django-'

        for match in re.findall(pattern, package_name):
            thefile.write("%s\n" % package_name.encode('utf-8'))


def list_finder():
    # diffile = open("dif.txt", 'w')
    for item in new_package_list:
        for link in soup.find_all('a', href=True, text=item):
            package_url_list.append(link['href'])
            return package_url_list


def new_to_old():
    with open(new) as f:
        with open(old, "w") as f1:
            for line in f:
                f1.write(line)


def mail_content():
    for el in package_url_list:
        r = requests.get(el)
        data = r.text
        new_soup = BeautifulSoup(data, "html.parser")

        para = new_soup.find('div', class_='section').find('p')
        name = new_package_list[package_url_list.index(el)].decode('utf-8')
        description = para.text
        description.decode('utf-8')
        pypi_url = el.decode('utf-8')

        message = name+"\n"+description+"\n"+pypi_url
        mail_content_list.append(message)

        return mail_content_list

new_package_list = difference()