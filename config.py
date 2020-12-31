####################################
## ./job-search-tool               #
## /config.py                      #
##                                 #
## @ author BCnBC                  #
## @ date 2020-12-30               #
## @ last-edited 2020-12-30        #
##                                 #
## v1.0.0                          #
##                                 #
##                                 #
####################################

import requests
from urllib.parse import urlparse
from urllib.parse import urlencode
from bs4 import BeautifulSoup

# create site search class
class site_search:
    
    # initialize variables
    def __init__(self, url):
        self.site_url = url
        
    # check for site form
    def is_site_form(self):
        formExists = False
        
        self.page = requests.get(self.site_url)
        
        return formExists
        
# create and format example url
my_url = r'https://www.indeed.com/jobs?'
query_vals = {'q':'Software Engineer',
              'l':'Sicklerville, NJ 08081',
              'radius': 50,
              'jt':'fulltime'}

my_url += urlencode(query_vals)

# test class
site1 = site_search(my_url)
site1.is_site_form()
print(site1.page.content)
