###########################
# ./job-search-tool       #
# /scrape.py              #
# @ author BCnBC          #
# @ Date 2020-12-30       #
# @ Last edit 2021-01-05  #
#                         #
#                         #
# v1.0.0                  #
#                         #
###########################

import config as cfg
import requests

class scraper:
    
    # define constructor
    def __init__(self, **sites):

        ## define empty dict for object site searches
        self.sites = {}
    
        ## add kwarg sites to self.sites dict
        if sites:
            for site in sites:
                self.sites[site] = sites[site]
    
    # define func to getContent of site_search object's page
    def getPageContent(self, site_index):
        self.page = requests.get(self.sites[site_index].get_req_endpoint())
        return self.page.content
    
    # return dict of scraper's sites
    def getSites(self):
        return self.sites

# test scraper object
if __name__=="__main__":
  
  ided = cfg.site_search(cfg.t_url)
  t_scraper = scraper(indeed=ided)
  t_scraper.sites["indeed"].set_params(cfg.t_payload)
  [print(t_scraper.getSites()[site]) for site in t_scraper.getSites()]
  print(t_scraper.getPageContent("indeed"))
  
            
        
    
    