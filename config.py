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
        
# create example url
my_url = r'https://www.indeed.com/jobs?q={query}&l={where}&radius={rad}&jt={type}'
query_vals = {'query':''}

# test class
site1 = site_search(my_url)
