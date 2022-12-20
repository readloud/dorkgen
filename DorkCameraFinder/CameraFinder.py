## Reecepbcups - January 17th, 2019
## Discord: Reecepbcups#3370

# Be sure to pip install google OR pip3 install google
from googlesearch import search 
import requests

ips = [] # Blank list for Camera IP's

def get():
    
# list of google dorks to scan
  dorks = ["""inurl:indexFrame.shtml Axis""",
    '''inurl:view/view.shtml?videos''',
    '''inurl:”CgiStart?page=”''',
    '''inurl:/view.shtml''',
    '''inurl:ViewerFrame?M0de=''',
    '''inurliaxis-cgi/jpg''',
    '''intitle:”live view” intitle:axis''',
    '''intitle:”Live NetSnap Cam-Server feed”''',
    '''intitle:”Live View/ — AXIS 210?''',
    '''intitleisnc-220 inurl:home/''',
    '''intitle:”Toshiba Network Camera” user Iogin''',
    '''jpegpull.htm''']

# If google ask for a captcha, it will fail.
# Just close the program and re-op if this happens, or
# run on http://repl.it > python 
  for query in dorks:
    try:
      for j in search(query, tld="com", num=100, stop=1, pause=1): 
        ips.append(j)
    except:
      print('failed on: ' + query)
      pass


# output the ips into text files
def output():
    
# Things to ignore that are not actual webcams
  ignore_list = ['alibaba','gov','fda','edu','amazon','ebay','shop']

  for item in ips: # grabs a camera ip/domain
      
      if item in ignore_list: # checks if it has the list, if so ignore 
          pass
      
      else: # output into the files
          with open('ips.txt', 'a') as f:
              f.write(item + "\n")
              f.close()

          if 'gov' in item:
              with open('government_sites.txt', 'a') as f:
                f.write(item + "\n\n")
                f.close()

          if 'edu' in item:
              with open('school_sites.txt', 'a') as f:
                f.write(item + "\n\n")
                f.close()
