import urllib2
from bs4 import BeautifulSoup

a = 'https://www.poetryfoundation.org/poems/92195/matilda-gathering-flowers'
b = 'https://www.poetryfoundation.org/poems/45113/alastor-or-the-spirit-of-solitude'
c = 'https://www.poetryfoundation.org/poems/45123/hymn-to-intellectual-beauty'
d = 'https://www.poetryfoundation.org/poems/45117/the-cloud-56d2247bf4112'
e = 'https://www.poetryfoundation.org/poems/45121/hellas-chorus'

poems = [a, b, c, d , e]
html = ""
poem_output = ""

for item in poems:
    response = urllib2.urlopen(item)
    html += response.read()

response.close

poem_input = BeautifulSoup(html, 'html.parser')
poem_output = poem_input.get_text()
