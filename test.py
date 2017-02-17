#!/usr/bin/python
import urllib2
def get_link(url):
    code = 0
    while code != 200:
        try:
            print url
            response = urllib2.urlopen(url)
            code = response.getcode()
            print code
            print response.read()
        except:
            pass

get_link("http://vnexpress.net")
