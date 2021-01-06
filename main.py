import requests 
from bs4 import BeautifulSoup as bs

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "cp1254,ISO-8859-9,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "tr,tr-TR,en-US,en;q=0.8",
}  

username = "coder_arena"#username of the account that you want to get the data from

if len(username)!=0:
    url = f"https://instagram.com/{username}"
    
else:
    print("please enter a username")

re = requests.get(url,headers=headers)

soup =bs(re.text,"html.parser")#you can use any parser you want to like xlml or html5lib
followers = soup.find_all("a",class_="-nal3 ")

for i in followers:
    print(i)