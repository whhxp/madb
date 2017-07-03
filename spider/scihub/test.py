#python scihub.py -d 10.1002/2015WR017349
# from scihub import SciHub

# sh = SciHub()

# # fetch specific article (don't download to disk)
# # this will return a dictionary in the form
# # {'pdf': PDF_DATA,
# #  'url': SOURCE_URL,
# #  'name': UNIQUE_GENERATED NAME
# # }
# result = sh.fetch('http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1648853')
# print(result)
###search

from scihub import SciHub

sh = SciHub()

# retrieve 5 articles on Google Scholars related to 'bittorrent'
results = sh.search('high entropy alloys', 2)

# download the papers; will use sci-hub.io if it must
for paper in results['papers']:
	sh.download(paper['url'])
#######################
# from scihub import SciHub
#
# sh = SciHub()

# exactly the same thing as fetch except downloads the articles to disk
# if no path given, a unique name will be used as the file name
#result = sh.download('http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1648853', path='paper.pdf')
#result = sh.download('10.1002/2015WR017349', path='test.pdf')