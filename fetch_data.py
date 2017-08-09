import urllib2

response = urllib2.urlopen('http://www.catb.org/esr/faqs/hacker-howto.html')
html = response.read()

response.close
