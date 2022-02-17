![GHDB ICON](https://i.ibb.co/dtn1Lfd/Webp-net-resizeimage-1.png)

# Intermezzo


A few moments ago I was mentored by Digit Oktavianto about Cyber Threat Methods, on that opportunity I was told about Google Dorking. He inspired me to create a tools that can automatically check web vulnerabilities by leveraging the Google Hacking Database from Exploit-DB. This tools also can be used as early warning system for system security based on update information from Google Hacking Database [Exploid-DB]. Once again I am very grateful about sharing experiences together.

Tools preview:<br>
<img src="https://i.ibb.co/5jyz7tH/hasil.png" width="80%"><br>

After processing using Elastic and Kibana<br>
<img src="https://i.ibb.co/pX5gtkH/ghdbgambar.png" width="80%">

## Methods

The techniques used in this tool are as follows:

- Crawling Google Hacking Database from Exploit-DB
- Using crawling results and combines with the target domain to become a search keyword
- Crawling Google Result based on keyword using [Barbarossa](https://github.com/nalonal/barbarossa)
- Display results on screen or save to file

## Requirements
- Python > 3.6
- I try this tools in Windows OS.



# Installation

## 1.Clone and Install Requirements

    git clone https://github.com/nalonal/ghdb.git
    cd ghdb
    pip install -r requirements.txt



## 2.Running Script to Create Cookie.txt File
Run the python script

    python ghdb.py

![create token file](https://i.ibb.co/0c3q2LF/createfile.png)

## 3.Copy Facebook Developer Tools Token to Cookie.txt
open [Facebook Developers Tools](https://developers.facebook.com/tools/) in browser and press Ctrl+i or Ctrl+Shift+i
![enter image description here](https://i.ibb.co/zPjp4WT/cookie.png)
Open file cookie.txt and paste Facebook Developers Tools Cookie to string text paste_here_without_enter

## 4.Create ghbdb.txt Database and Update Google Hacking Database from Exploit
Run again python script

    python ghdb.py

After update cookie success then system will update GHDB and produce ghdb.txt it will take about 1-2 minute
![enter image description here](https://i.ibb.co/kMMWr8G/update-ghdb.png)

## 5.Running File

### 5.1 Running GHDB Dorking

Running help

    python ghdb.py -h

Running GHDB but just print screen the result

    ghdb.py -d <domain or list domain separate using ',' or you can use file with .txt extension>
    example: ghdb.py -d example.com
    example: ghdb.py -d example1.com,example2.com
    example: ghdb.py -d mylistdomain.txt

Running GHDB and save the result to file

    ghdb.py -d <domain or list domain separate using ',' or you can use file with .txt extension> -o <outputfile>
    example: ghdb.py -d example.com -o result.txt
    example: ghdb.py -d example1.com,example2.com -o result.txt
    example: ghdb.py -d mylistdomain.txt -o result.txt

### 5.2 Running SQLi Dorking

Running help

    python sqli.py -h

Running GHDB but just print screen the result

    sqli.py -d <domain or list domain separate using ',' or you can use file with .txt extension>
    example: sqli.py -d example.com
    example: sqli.py -d example1.com,example2.com
    example: sqli.py -d mylistdomain.txt

Running GHDB and save the result to file

    sqli.py -d <domain or list domain separate using ',' or you can use file with .txt extension> -o <outputfile>
    example: sqli.py -d example.com -o result.txt
    example: sqli.py -d example1.com,example2.com -o result.txt
    example: sqli.py -d mylistdomain.txt -o result.txt


# Disclaimer
This script is used as an early warning system based on updating information from the Google Hacking Database [Exploit-DB]. Please use it as wisely as possible

