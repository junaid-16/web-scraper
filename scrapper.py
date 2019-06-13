import requests
from bs4 import BeautifulSoup
from googlesearch import search
import csv


url = 'https://blockchain-expo.com/europe/speakers/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#creating a csv file
f = csv.writer(open('file.csv','w'))
f.writerow(['event: blockchain-expo'])
f.writerow(['name','pic','designation','company','linkedin','twitter','wikipedia','facebook']) 

for data in content.findAll('div', attrs={"class":"speaker-expand clearfix"}):
	#name
	name= data.find('h3').text
	#pic
	pics= data.find('img')
	pic=(pics.get('src'))
	#designation and company
	designation_company = data.findAll('h4')
	designation=designation_company[0].text
	company=designation_company[1].text
	#linkedin
	linkedin=name + "linkedin"
	for i in search(linkedin, tld="co.in", num=1, stop=1, pause=2):
		l_url=i
	#twitter
	twitter=name + "twitter"
	for i in search(twitter, tld="co.in", num=1, stop=1, pause=2):
		t_url=i
	#wikipedia
	wikipedia= name + "wikipedia"
	for i in search(wikipedia, tld="co.in", num=1, stop=1, pause=2):	
		wiki=i
	#facebook
	facebook = name + "facebook"
	for i in search(facebook, tld="co.in", num=1, stop=1, pause=2):
		fb=i


	#writing the data on csv file
	l=[name,pic,designation,company,l_url,t_url,wiki,fb]
	f.writerow(l
