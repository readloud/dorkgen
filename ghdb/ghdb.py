import requests, time, re, os, sys, getopt
from os import system, name
from datetime import date
from pyfiglet import Figlet
from barbarossa import google
from datetime import date

##init
file_name_cookie = "cookie.txt"
file_name_ghdb = "ghdb.txt"
file_name_running = "ghdb.py"

def prRed(skk): return("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): return("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): return("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): return("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): return("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): return("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): return("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): return("\033[98m {}\033[00m" .format(skk)) 

def update_info(file_name_ghdb):
	with open(file_name_ghdb, encoding="utf-8") as fp:
		line = fp.readline()
		print("Update date GHDB : "+str(line.strip("\n"))+" (to update database please delete file "+file_name_ghdb+")")

def check_args():
	if(len(sys.argv) <= 1):
		help()
		exit()
def listToString(s):  
    str1 = "  " 
    return (str1.join(s))

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def clear(): 
	if name == 'nt': 
	    _ = system('cls') 
	else: 
	    _ = system('clear')

def parse_cookie(file_name):
	output = {}
	f = open(file_name, "r")
	read_file = f.read().split("\n")
	output['facebook_devtools'] = read_file[0].replace("cookie_facebook_devtools =","").replace(" ","")
	if(output['facebook_devtools'] == "paste_here_without_enter" or output['facebook_devtools'] == ""):
		return False
	else:
		return output

def create_token(file_name):
	with open(file_name, 'a', newline='\n', encoding="utf-8") as this_file:
		print("Generate token file, please upload your https://developers.facebook.com/tools Cookies in "+file_name)
		this_file.write("cookie_facebook_devtools = paste_here_without_enter")
	exit()

def welcome():
	clear()
	print(Figlet(font='slant').renderText('GoogleHackDB'))
	print('Tools for checking website from Google Dorking Issue\nCheck github : https://github.com/nalonal/ghdb')

def func_request(headers, this_draw, this_page, perpage, this_id):
	this_url = "/google-hacking-database?draw="+str(this_draw)+"&h%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start="+str(this_page)+"&length="+str(perpage)+"&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&category=&&draw=3&columns%5B0%5D%5Bdata%5D=date&columns%5B0%5D%5Bname%5D=date&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=url_title&columns%5B1%5D%5Bname%5D=url_title&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=cat_id&columns%5B2%5D%5Bname%5D=cat_id&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=author_id&columns%5B3%5D%5Bname%5D=author_id&columns%5B3%5D%5Bsearchable%5D=false&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start="+str(this_page)+"&length="+str(perpage)+"&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&category=&_="+str(this_id)
	headers['path'] = this_url
	web = requests.get("https://www.exploit-db.com"+this_url, headers=headers)
	return web.json()

def crawler():
	headers = {
		'authority': 'www.exploit-db.com',
		'method': 'GET',
		'path': '/google-hacking-database?draw=4&columns%5B0%5D%5Bdata%5D=date&columns%5B0%5D%5Bname%5D=date&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=url_title&columns%5B1%5D%5Bname%5D=url_title&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=cat_id&columns%5B2%5D%5Bname%5D=cat_id&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=author_id&columns%5B3%5D%5Bname%5D=author_id&columns%5B3%5D%5Bsearchable%5D=false&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&category=&_=1603177183181',
		'scheme': 'https',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		# 'cookie': str(cookie),
		'referer': 'https://www.exploit-db.com/google-hacking-database',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}

	filename = file_name_ghdb
	this_page = 0
	page = 1
	perpage = 120
	this_id = 1603177871161
	this_draw = 1
	this_total = 1

	if os.path.exists(filename):
		try:
			os.remove(filename)
		except OSError:
			pass
	with open(filename, 'a', newline='\n', encoding="utf-8") as this_file:
		print("Update database, please wait until process success (maybe 1-2 minute)...")
		print("note:if process interupt or failed please delete "+file_name_ghdb+" and restart process")
		today = date.today()
		this_file.write(today.strftime("%Y-%m-%d")+"\n")
		while True:
			value = func_request(headers, this_draw, this_page, perpage, this_id)
			for per_data in value['data']:
				input_value = str(per_data['id'])+'   '+str(per_data['date'])+'   '+str(cleanhtml(per_data['url_title']))+'   '+str(per_data['author_id'][1])+'   '+str(per_data['category']['cat_title'])+'   '+str(per_data['category']['cat_description'])
				this_file.write(input_value+"\n")
				print("\r", "Get "+str(this_total)+" data from https://www.exploit-db.com/google-hacking-database", end="")
				this_total += 1		
			if(len(value['data']) < perpage):
				break
			this_id += 1
			this_page = this_page+perpage
			page += 1
	print("\nUpdate Success")
	return True

def check_registration():
	welcome()
	if os.path.exists(file_name_cookie) == False:
		print("File manager for cookie https://developers.facebook.com/tools not exist")
		input_update = input("please create file and paste the cookie(y/n):")
		if(input_update == 'y'):
			create_token(file_name_cookie)
			exit()
		else:
			welcome()
			print('Sorry but this tools is useless without cookie')
			exit()

	if (parse_cookie(file_name_cookie) == False):
		welcome()
		print('Sorry please copy your https://developers.facebook.com/tools cookie in '+file_name_cookie)
		exit()

	if os.path.exists(file_name_ghdb) == False:
		input_update = input("GHDB database not exists, please update (y/n):")
		if(input_update == 'y'):
			crawler()
			exit()
		else:
			welcome()
			print('Sorry but this tools is useless without GHDB database')
			exit()

def help():
	welcome()
	print("\nHow to use this tools:")
	print ("   "+file_name_running+" -d <domain or list domain separate using ','>")
	print ("   "+file_name_running+" -d <domain or list domain separate using ','> -o <outputfile>")


def read_all_ghdb(file_name_ghdb, perdomain):
	with open(file_name_ghdb, encoding="utf-8") as fp:
		line = fp.readline() ## skip for date
		line = fp.readline()
		cnt = 1
		while line:
			per_data = line.split("   ")
			dorking_text = per_data[2]
			dorking_category = per_data[4]
			for persearch in google(parse_cookie(file_name_cookie)['facebook_devtools'],"site:"+perdomain+" "+dorking_text,1):
				print("["+dorking_category+"] "+dorking_text+"   "+persearch['url'])
			cnt = cnt+1
			line = fp.readline()

def read_write_all_ghdb(file_name_ghdb, perdomain, outputfile):
	file = open(file_name_ghdb, "r", encoding="utf-8")
	line_count = 0
	for line in file:
	    if line != "\n":
	        line_count += 1
	file.close()
	with open(file_name_ghdb, encoding="utf-8") as fp, open(outputfile, 'a', newline='', encoding="utf-8") as writefile:
		line = fp.readline() ## skip for date
		line = fp.readline()
		cnt = 1
		writefile.write("Google dorking for "+perdomain+" [Dorking Date:"+date.today().strftime("%Y-%m-%d")+"]\n")
		while line:
			per_data = line.split("   ")
			dorking_text = per_data[2]
			dorking_category = per_data[4]
			print(prPurple("[Process "+str(format((cnt/line_count)*100, ".2f"))+"%]")+"   ")
			for persearch in google(parse_cookie(file_name_cookie)['facebook_devtools'],"site:"+perdomain+" "+dorking_text,1000):
				this_output_print = prGreen("[")+prGreen(dorking_category)+prGreen("]   ")+dorking_text+"   "+prYellow(persearch['url'])+"   "+"detail_ghdb_info:["+listToString(per_data).strip("\n")+"]"
				print(this_output_print)
				this_output = "["+dorking_category+"]"+"   "+dorking_text+"   "+persearch['url']+"   "+"detail_ghdb_info:["+listToString(per_data).strip("\n")+"]"
				writefile.write(this_output+"\n")
			cnt = cnt+1
			line = fp.readline()
		writefile.write("\n")

def run_domain(inputdomain, outputfile):
	if(inputdomain.find(".txt") != -1):
		with open(inputdomain, encoding="utf-8") as fp:
			list_domain = []
			line = fp.readline()
			while line:
				list_domain.append(line.replace("\n",""))
				line = fp.readline()
	else:
		list_domain = inputdomain.split(",")
	if(outputfile == ""):
		for perdomain in list_domain:
			print("Search dorking issue for site:"+perdomain)
			read_all_ghdb(file_name_ghdb, perdomain)
	else:
		for perdomain in list_domain:
			print("Search dorking issue for site:"+perdomain)
			read_write_all_ghdb(file_name_ghdb, perdomain, outputfile)

def main(argv):
	inputfile = ''
	outputfile = ''
	check_registration()
	check_args()
	update_info(file_name_ghdb)
	try:
		opts, args = getopt.getopt(argv,"hd:o:",["domain=","ofile="])
		for opt, arg in opts:
			if opt == '-h':
				help()
				sys.exit()
			elif opt in ("-d", "--domain"):
				inputdomain = arg
			elif opt in ("-o", "--ofile"):
				outputfile = arg
		run_domain(inputdomain,outputfile)

	except getopt.GetoptError:
		help()
		print('\nWarning: Error Command')
		sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])