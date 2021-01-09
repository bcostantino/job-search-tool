import config as cfg
import scrape

# ex commands:
#
# crt_scanner -n:new_sc

class scanner():
    def __init__(self, _iter=0):
        # scanner constructor
        self.quit=False
        
        if _iter>0:
            cmd = input(">> ")
            
        else:
            cmd = input("Enter a command *type help for command list*:\n>> ")
            
        if cmd == "help":
            print("crt_ scrape: creates a new scraper for user \nadd_site:adds a new site for scraper to scrape \nadd_param: adds parameter such as salaries/location/etc")
        
        elif "crt" in cmd:
            
            # parse_crt(cmd) will parse a create scraper command to find necessary arguments (name)
            new_sc_name = self.parse_crt(cmd)
            
            # create new scraper object
            new_scraper = scrape.Scraper(new_sc_name)
            
            print("New Scraper() named: "+new_sc_name+" successfully created")
            
        elif "quit" in cmd:
            self.quit = True
            
        elif cmd == "add_site":
            
            
            #just tell me if this is what you want
            print(self.site_name + "added")
            
        elif cmd == "add_param": #can we have a param check to see if it is valid
        
            print(self.param_name + "added")
    
    def parse_crt(self, cmd):
        
        syntax = cmd.split('-')
        new_scr_name = syntax[-1][2:].capitalize()
        
        return new_scr_name
    
    def parse_cmd(self, cmd):
        if "crt_scrape" in cmd:
            syntax=cmd.split('-')
            new_scr_name=syntax[-1][2:].capitalize()
            
        elif "add_site" in cmd:
            syntax=cmd.split('-')
            self.scraper_name=syntax[1][2:].capitalize()
            self.site_name=syntax[-1][3:].capitalize()
            pass
        elif "add param" in cmd:
            pass
        elif "help" in cmd:
            pass
        elif "quit" in cmd:
            pass
    
    def create_object(self, _type, inst_name):
        if _type==0:     # Scraper()
            pass
        elif _type==1:   # site_search()
            pass
        else:
            pass
    
if __name__=="__main__":
    _iter = 0
    while True:
        sc = scanner(_iter)
        _iter+=1
        
        if sc.quit:
            break
        