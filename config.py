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
    
my_url = r'https://www.indeed.com/?sq=1'
site1 = site_search(my_url)
        