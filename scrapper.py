from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url='https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&as-pos=0&as-type=HISTORY&suggestionId=iphone&requestId=4a1b1a02-4639-4f9c-8f49-f09846a00303'

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers= page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})

# print(len(containers))

#print(soup.prettify(containers[0]))

container=containers[1]
print(soup.prettify(container))

# price = container.findAll("div", {"class": '_3wU53n'})
# print(price)

