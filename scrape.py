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
from bs4 import BeautifulSoup

class Scraper:
    
    # define constructor
    def __init__(self, name="NI", **sites):
        
        # init scraper name
        self.name = name

        # define empty dict for object site searches
        self.sites = {}
    
        # add kwarg sites to self.sites dict
        if sites:
            for site in sites:
                self.sites[site] = sites[site]
                
    def __str__(self):
        sites_rep = ''
        for site in self.sites:
            sites_rep += str(site)
        
        return "Name: "+self.name+"\nSites: "+sites_rep
    
    # define func to getContent of site_search object's page
    def getPageContent(self, site_index='A'):
        
        # if site_index == 'A' get content for all sites
        if site_index=='A':
            pages = []
            [pages.append(requests.get(self.sites[site].get_req_endpoint()).content) for site in self.sites]
            return pages
        
        elif site_index in self.sites.keys():
            page = requests.get(self.sites[site_index].get_req_endpoint())
            return page.content
        
        else:
            return False
    
    # define func to find listings on page
    def findListings(self, site_index='A'):
        
        # if site_index == 'A' get listings on every site
        if site_index=='A':
            divss = []
            for key in self.sites:
                pass
        
        elif site_index in self.sites.keys():
            page = self.getPageContent(site_index)
            soup = BeautifulSoup(page, features="html.parser")
            divs = soup.findAll("div", {"class": "jobsearch-SerpJobCard unifiedRow row result clickcard"})
            
            return divs
    
    # return dict of scraper's sites
    def getSites(self):
        return self.sites
    
    

# test scraper object
if __name__=="__main__":
    # create and format test url
    t_url = r'https://www.indeed.com/jobs?'

    # test payload
    t_payload = {'ql':'Software Engineer',
                'sal':'70,000',
                'l':'Sicklerville, NJ 08081',
                'radius': 50,
                'jt':'fulltime'}
  
    # create site search object
    ided = cfg.site_search(t_url)
    
    # create scraper object and pass ided site search
    t_scraper = Scraper(name="tscraper", indeed=ided)
  
    # set parameters for site search object
    t_scraper.sites["indeed"].set_params(t_payload)
  
    # print all of scraper's sites
    [print(t_scraper.getSites()[site].get_req_endpoint()) for site in t_scraper.getSites()]
  
    print(t_scraper)
    print(t_scraper.getPageContent("indeed"))
  
  
            
        
    
    