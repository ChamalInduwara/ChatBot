import urllib.request
import xarray as xr
import io
from googlesearch import search


def reading_url(link):
    url = link

    f = urllib.request.urlopen(url)
    txt = open('read.html', 'w').write(str(f.read()))

    return 'read \'read.html\''


def search_for_link(mzg):
    query = mzg
    link_array = []
    for j in search(query, tld='co.in', num=10, stop=10, pause=2):
        link_array.append(j)

    return reading_url(link_array[0])
    # return link_array


inp = input(': ')
print(search_for_link(inp))
# print(reading_url(None))

