## Reecepbcups - December 10th, 2018.
## Discord: Reecepbcups#3370

# A python app to scan google dorks and gather network cameras to homes, businesses, and the Government
# Ex. http://camera.buffalotrace.com/view/view.shtml?id=92509&imagePath=/mjpg/video.mjpg&size=1

# ---------------------------------------------------------------------------------
# THIS SOFTWARE HAS LITTLE TESTING, BUT IS MORE OPTOMIZED. USE "Camera_Finder.py" 
# in the main area to run the less efficent code, but more reliable 
# ---------------------------------------------------------------------------------

try:
  
  from googlesearch import search 
  import requests
  print('Modules Imported successfully\n -= You can run getCams() to start =-')
  
except:
  print('!!Install google and requests modules!!')
  print('Open CMD >> pip install -r requirements.txt')


        
ips = [] # blank list for the ips to go into

def getCams():
  global ips # makes sure "ips" variable can be used elsewhere

  dorks = [
    "inurl:indexFrame.shtml Axis",
    "inurl:view/view.shtml?videos",
    "inurl:”CgiStart?page=”",
    "inurl:/view.shtml",
    "inurl:ViewerFrame?M0de=",
    "inurliaxis-cgi/jpg",
    "intitle:”live view” intitle:axis",
    "intitle:”Live NetSnap Cam-Server feed”",
    "intitle:”Live View/ — AXIS 210?",
    "inurl:/mjpg/video.mjpg",
    "inurl:/view/view.shtml",
    "inurl:/view/view.shtml"
    ]

  for camera in dorks: # loops though the above list and gets ips/domains of network cameras.
    try:
      # for links in search results, using google.com
      ips = [link for link in search(camera, tld="com", num=100, stop=1, pause=1)]
      
    except:
      print('Failed on: ' + camera)
      print('HTTP Error 503: Google has blocked you from more searches.\nTry using https://repl.it/languages/python3 OR a VPN\n')
      pass

  return ips


def output():
  junkLinks = ['alibaba', 'amazon', 'ebay', 'shop'] # just selling cameras, put junk here
  
  for item in ips:
    if item not in junkLinks:
      with open('IP_Cameras.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()

    if 'gov' in item:
      with open('Government_Cameras.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()

    if 'edu' in item:
      with open('EDU_Cameras.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()
        
    if 'com' in item:
      with open('Comercial_Cameras.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()
