import urllib2
request = urllib2.Request(
    r'http://books.google.de/books?id=gikDAAAAMBAJ&pg=PA1&img=1&w=2500',
    headers={'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 firefox/2.0.0.11'})
page = urllib2.urlopen(request)

with open('somefile.png','wb') as f:
    f.write(page.read())
    