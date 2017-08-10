import urllib2

a = 'https://www.poetryfoundation.org/poems/92195/matilda-gathering-flowers'
b = 'https://www.poetryfoundation.org/poems/45113/alastor-or-the-spirit-of-solitude'
c = 'https://www.poetryfoundation.org/poems/45123/hymn-to-intellectual-beauty'
d = 'https://www.poetryfoundation.org/poems/45117/the-cloud-56d2247bf4112'
e = 'https://www.poetryfoundation.org/poems/45121/hellas-chorus'

poems = [a, b, c, d , e]

for item in poems:
    response = urllib2.urlopen(item)
    html += response.read()

print html

response.close
