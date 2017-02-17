#!/usr/bin/python
import urllib2
response = urllib2.urlopen('http://localhost:8080/api')
print response.getcode()
print response.read()

