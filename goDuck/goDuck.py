#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from proxybroker import Broker
from urllib.parse import unquote
import requests
import sys
import random
import asyncio
import urllib3
import time
import getopt
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Some aux variables and global  stuff u know, to do shit.
proxie_num=5
pool={}
gold=[]
sleeper=3

URLS = [ "https://duckduckgo.com/html/?q=inurl:{} ({})&t=lm&ia=web",
         "https://duckduckgo.com/lite/?q=inurl:{} ({})&t=lm&ia=web" ]

HTTP_ERR = {
            301:'HTTP_STATUS: 301 - Moved Permanently',
            307:'HTTP_STATUS: 307 - Temporary Redirect',
            401:'HTTP_STATUS: 401 - Unauthorized',
            402:'HTTP_STATUS: 402 - Payment Required. The webserver says:Drop your wallet now!!',
            403:'HTTP_STATUS: 403 - Forbidden, holy fuck, what are u doing?',
            406:'HTTP_STATUS: 406 - Not Acceptable. oh my tux lord, WHY?',
            429:'HTTP_STATUS: 429 - Too many requests',
            503:'HTTP_STATUS: 503 - Service Unavailable',
            504:'HTTP_STATUS: 504 - Gateway Timeout'
            } 

# Functions and stuff like that
def usage():
    print("""Welcome to goDuck, the badass google hacking gambiarra using DDG
    We will try to perform inurl parameter to get some links.
    Options:
     -q -> Query String
     -f -> A File with dorks separete by line
     -o -> output file
    Here some usage examples:
       If you want to search by a single dork:
         ./goduck.py -q "db/CART/product_details.php?product_id="
         ./goduck.py -q "shopreviewadd.php?id="
         ./goduck.py -q "global/product/product.php?gubun="
       If you want to search using a file filled with dorks:
         ./goduck.py -f /path/to/file
         ./goduck.py -f file.txt
         ./goduck.py -f file
 
        -o Using output option
         ./goduck.py -f file -o logs.txt
    Thats All morty!
       """)
    exit(1)

def banner():
    print('''
             ____             _    
  __ _  ___ |  _ \ _   _  ___| | __
 / _` |/ _ \| | | | | | |/ __| |/ /
| (_| | (_) | |_| | |_| | (__|   < 
 \__, |\___/|____/ \__,_|\___|_|\_\
 |___/                             

                                https://github.com/d34dfr4m3/goDuck
    ''')

def get_country():
    country_list = ['BR','US','RU','AR','CL']
    return random.choice(country_list)

def get_ua():
  ua_list = [  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
               'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0']
  return random.choice(ua_list)

def check_proxy(proxy):
  try:
    data=requests.get('https://api.ipify.org?format=json',timeout=30,allow_redirects=True,proxies=proxy,verify=False)
  except Exception as error:
    print('[!!] Check Proxy Error: ' + str(error))
    return False
  if data.status_code == 200:
    if data.text.split('"')[3] == proxy['https'].split(':')[0]:
      print('[+] Proxy OK - External IP is ' + data.text.split('"')[3])
      return True

# Function to grab proxies
async def show(proxies):
  global pool
  global sleeper
  while True:
    proxy = await proxies.get()
    if proxy is None: break
    pool[str(proxy).split(']')[1].strip('>').split(':')[0].strip()]=str(proxy).split(']')[1].strip('>').split(':')[1]

# Function to start the another function to grab proxies.
def proxypool(generate=None,proxie_num=5):
  global sleeper
  global pool
  if generate:
    print("[+] Building a new proxy pool")
    proxies = asyncio.Queue()
    broker=Broker(proxies)
    country=get_country()
    print('[-] Colecting proxies from country: '+ country)
    tasks=asyncio.gather(broker.find(types=['HTTPS'],country=[country], limit=proxie_num),show(proxies))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    print("[+] Pool got %s proxies" %(len(pool)))
    return True
  elif len(pool) == 0:
    print("[!] Proxy Pool is empty, please wait while we build more")
    proxie_num = sleeper
    proxypool(True,proxie_num)
    sleeper=5
    # Dict format: {(‘192.168.0.1’, ‘80’, (‘HTTP’, ‘HTTPS’), …)}
  for ip, port in pool.items():
    print("[+] Proxy %s:%s selected" %(ip,port))
    proxyReady={}
    proxyReady['https'] = str(ip+':'+port)
    del pool[ip]
    return proxyReady

def get_page(URL,proxie):
  if not check_proxy(proxie):
    return False
  cookie = {'p': '-2',
            'ah':'br-pt'}
  headers={
    'User-Agent':'',
    'Accept': 'text/html',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en-US,en;q=0.5',
#    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control':'no-cache'
  }
  headers['User-Agent']=get_ua()
  try:
    r=requests.get(URL,headers=headers,timeout=30,allow_redirects=True,cookies=cookie,proxies=proxie,verify=False)
    if r.status_code == 200:
      return r
    elif r.status_code in HTTP_ERR:
      print('[!!] '+HTTP_ERR[r.status_code])
      return False
    else:
      print("[*] HTTP_CODE %s Error:" %s(str(r.status_code)))
      print(r.text)
      return False
  except KeyboardInterrupt:
      print("[!] User interrupt Ctrl^c, Aborting  noOOOOWW")
      exit(1)
  except Exception as error:
    print("[*] Request Error:" + str(error))
    return False

def main(search=None,outf=None):
  global sleeper 
  count=1
  proxypool(generate=True)
  print("[!] - Query: "+search)
  page=get_page(random.choice(URLS).format(search,search),proxypool())
  while not page:
    print("[+] - Busted, wainting %s seconds" %(sleeper))
    time.sleep(sleeper)
    print("[=] - Going to next proxy")
    sleeper=sleeper+sleeper
    page=get_page(random.choice(URLS).format(search,search),proxypool())
  
  soup = BeautifulSoup(page.content, 'html5lib')
  query=soup.title.content
  for link in soup.find_all('a',class_='result__url'):
    link_href=link.get('href')
    if link_href is not None:
      link_href=unquote(link_href)
      if 'uddg' in link_href: 
        link_href = link_href.split('=')[2]
      if 'http' in link_href or 'https' in link_href:
        if link_href not in gold:
          gold.append(link_href)

  if len(gold) == 0:
    print("[!!] Got 0 Results. Going to next try %s/3 " %(count))
    main(search)
    count+=1
    if count >= 3:
      print("[!] BAD LUCK")
  else: 
    if query:
      if outf:
         outf.write('[*] Dumping %s results from query: %s \n' %(len(gold),query))
      print('[*] Dumping %s results from query: %s ' %(len(gold),query))
    else:
      if outf:
         outf.write('[*] Dumping %s results from query: %s \n' %(len(gold),query))
      print('[*] Dumping %s results from query: %s ' %(len(gold),search))
    count=0
    sleeper=2
    for url_gold in gold:
      if outf:
         outf.write(url_gold+'\n')
      print("[--] "+url_gold)


if __name__ == "__main__":
  outputfile=None
  ListMode=None
  SingleMode=None
  banner()
  if len(sys.argv) <= 1:
    usage()
  try:
      opts,args = getopt.getopt(sys.argv[1:], "q:f:o:h")
  except getopt.GetoptError as err:
      print("[!!] Error in getopt: ", err)
      usage()
  for option, arg in opts:
    if option == "-q":
      SingleMode=True
      search=arg
    elif option == "-o":
      outputfile=arg
    elif option == "-f":
      ListMode=True
      fileread=arg
    elif option == '-h':
      usage()
    else:
      usage()
  print('check')
  if SingleMode and ListMode:
    print("[!] Dude, use -q or -f")
  elif SingleMode:
    outf=open(outputfile,'a')
    main(search,outf) 
    outf.close()
  elif ListMode:
    outputfile = arg
    f = open(fileread,'r')
    outf=open(outputfile,'a')
    for i in f:
        print(type(f))
    main(i,outf) 
    outf.close()
    f.close()