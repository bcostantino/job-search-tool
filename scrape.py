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

class scraper:
  def __init__(self, **sites):
    ## define empty dict for object site searches
    self.sites = {}
    if sites:
      for site in sites:
        self.sites[site] = sites[site]

# test scraper object
if __name__=="__main__":
  
  ided = cfg.site_search(cfg.t_url)
  my_scraper = scraper(indeed=ided)
  my_scraper.sites["indeed"].set_params(cfg.t_payload)
  [print(my_scraper.sites[site]) for site in my_scraper.sites]
            
        
    
    