# Copyright Anshuman73.
# Visit anshuman73.github.io for more info.
# Released under MIT License.
# Works with Python 2.7

import urllib
import os
from datetime import datetime
try:
	from bs4 import BeautifulSoup
except:
	import pip
	print 'Downloading dependency BeautifulSoup...'
	pip.main(['install', 'beautifulsoup4'])
	from bs4 import BeautifulSoup

def main():
	cwd = os.getcwd()
	print '\nChecking if /images directory exists..'
	if not os.path.exists(cwd + '/images'):
		print 'Making directory /images\n'
		os.makedirs(cwd + '/images')
	else:
		print '\ndirectory "/images" exists, moving on...\n'

	base_url = 'http://explosm.net'

	this_year = datetime.today().year
	this_month = datetime.today().month
	
	archives = []
	for month in xrange(this_month, 0, -1):
		archives.append('%s/%s' %(this_year, month))
	
	for year in xrange(this_year - 1, 2004, -1):
		for month in xrange(12, 0, -1):
			archives.append('%s/%s' %(year, month))

	for archive in archives:
		soup = BeautifulSoup(urllib.urlopen(base_url + '/comics/archive/' + archive).read(), 'html.parser')
		comics = soup.select('.past-week-comic-title')

		for comic in comics:
			link = base_url + comic.a['href']
			comic_soup = BeautifulSoup(urllib.urlopen(link).read(), 'html.parser')
			img_link = 'http:' + comic_soup.find('img', id='main-comic')['src']
			name = img_link[img_link.rfind('/') + 1:]

			if not os.path.exists(cwd + '/images/' + name):
				print 'Downloading image - ' + name
				urllib.urlretrieve(img_link.encode('utf8'), cwd + '/images/' + name)
			else:
				print 'The Image "' + name + '" already exists. Skipping...'

if raw_input('\nPress Enter to start:') == '':
	main()