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

######
#
# Library for web scraping job finder tool. Framework for web scraping in general.
# Brian C, Ben C
#
######

import requests
from urllib.parse import urlparse
from urllib.parse import urlencode
from bs4 import BeautifulSoup



# create site search class
class site_search:
    
    #######
    ## In order to register a site as a site search object, one must know ALL NECESSSARY query paramaters.
    ## The paramaters will be passed by paramater name(s). See self.set_params...
    #
    #    Example:
    #
    #    my_site = site_search(my_url, params={'q':'Software Engineer',
    #                                          'l':'Sicklerville, NJ 08081',
    #                                          'radius': 50,
    #                                          'jt':'fulltime'})
    #
    #######
    
    # initialize variables
    def __init__(self, url, params=False):
        self.site_url = url
        self.req_params = params
    
    # create object representation
    def __repr__(self):
        return f"site_search({self.site_url}, {self.req_params})"
    
    # create readable str format of object
    def __str__(self):
        return f"Endpoint: {self.site_url}\nParamaters: {self.req_params}"
    
    #######
    ## This function has two purposes, initializing, or changing paramaters. If self.req_params == False,
    ## object params are not set, and must be passes in as a dictionary object called params. To add new
    ## params to a preexisting dictionary, pass indivisual kwargs to a dict called **nn_params
    #######
    
    # function to set params if not initialized
    def set_params(self, params, **nn_params):
        
        # check paramater state
        if not self.req_params:
            self.req_params = params
        else:
            if nn_params:
                for key in nn_params:
                    self.req_params[key] = nn_params[key]
            else:
                return False
    
    # function to clear paramaters. specify specific param keys to remove as *args (i.e. *spc_params)
    def clr_params(self, *spc_params):
        if not spc_params:
            self.req_params = False
        else:
            [self.req_params.pop(key) for key in spc_params]
            
    
        
    
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


#my_url += urlencode(query_vals)

# test class
site1 = site_search(my_url)
site1.set_params(params={'q':'Software Engineer',
                          'l':'Sicklerville, NJ 08081',
                          'radius': 50,
                          'jt':'fulltime'})
print(site1)
site1.clr_params()
print(site1)
