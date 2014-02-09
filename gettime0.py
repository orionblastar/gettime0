# Writen by Orion Blastar 02/08/2014
# OrionBlastar@gmail.com http://blastar.in @OrionBlastar on Twitter
# Using the Beautiful Soup library and the URLLIB2 library this Python 2.7
# script reads a URL and then parses the HTML to find the current
# date and time. 
# Warning you have to install the Beautiful Soup library to make this work.
# If you don't know how to do that read a Python book and learn how PIP works.
# Written as a Demo for https://www.syndk8.com/ make sure to pay them guys and gals a visit
# This script was written in GNU/Linux, your milage may vary in Windoze or MacOSEcks
# If you don't know what GNU/Linux is, and only know Windoze, well stinks to be you!
#This script might work with Python 2.7 in Windoze if you remove the line below this comment.
#!/usr/bin/python
# -*- coding: latin-1 -*-
import urllib2
#from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())

for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string
    # will print date and sunrise
