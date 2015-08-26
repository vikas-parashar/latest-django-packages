from bs4 import BeautifulSoup
import re
import json

def difference(f1, f2):
	with open(f1) as f:
	    t1 = f.read().splitlines()
	    t1s = set(t1)

	with open(f2) as f:
	    t2 = f.read().splitlines()
	    t2s = set(t2)

	diff_list = []
	for diff in t2s-t1s:
		diff_list.append(diff)
	return diff_list


def package_finder():
	thefile = open("new.txt", 'w')
	for row in soup.find_all('a'):
		package_name = row.text
		pattern = 'django-'

		for match in re.findall(pattern, package_name):
			   thefile.write("%s\n" % package_name.encode('utf-8'))
	print "file created"

def list_finder():
	diffile = open("dif.txt", 'w')
	for item in new_package_list:
		for link in soup.find_all('a',href=True, text=item):
			print link['href']


soup = BeautifulSoup(open("pypi.html"), "html.parser")

package_finder()

f1='old.txt'
f2='new.txt'

new_package_list = difference(f1,f2)

list_finder()
