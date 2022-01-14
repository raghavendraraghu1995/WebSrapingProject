import requests
from bs4 import BeautifulSoup
URL="https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGN617M/ref=sr_1_4?dchild=1&keywords=Samsung+M31&qid=1627412024&sr=8-4"
headers = {
    "user_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html_parser')
product_price=soup.find(id='priceblock_dealprice')
print(product_price.getText())