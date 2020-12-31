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
    
    #######
    ## In order to register a site as a site search object, one must know ALL NECESSSARY query paramaters.
    ## The paramaters will be passed to the object as a  containing paramater name(s). 
    #######
    
    # initialize variables
    def __init__(self, url, params):
        self.site_url = url
        self.req_params = params
    
    # create object representation
    def __repr__(self):
        return f"site_search({self.site_url}, {self.req_params})"
    
    # create readable str format of object
    def __str__(self):
        return f"Endpoint: {self.site_url}\nParamaters: {self.req_params}"
        
    
    """
    ## Outdated
    #
    #   # check for site form
    #   def is_site_form(self):
    #       formExists = False
    #       
    #       # scrape site to find form
    #       self.page = requests.get(self.site_url)
    #       self.soup = BeautifulSoup(self.page.text, "html.parser")
    #       self.form = self.soup.find_all('form')
    #       
    #       for form in self.form:
    #           print(form.prettify())
    #       
    #       return formExists
    ##
    """


# create and format example url
my_url = r'https://www.indeed.com/jobs?'
query_vals = {'q':'Software Engineer',
              'l':'Sicklerville, NJ 08081',
              'radius': 50,
              'jt':'fulltime'}

#my_url += urlencode(query_vals)

# test class
site1 = site_search(my_url, query_vals)
print(site1)
