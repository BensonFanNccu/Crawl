from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import requests

def crawl_website(url):
    ua = UserAgent()
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find_all('h1', class_='title')
        detail_items = soup.find_all('div', class_='col-lg-9 order-lg-1 order-sm-2 order-2')
        
        for item in detail_items:
            p_tags = item.find_all('p')
            
            if p_tags:
                with open(file, 'w', encoding='utf-8') as f:
                    for t in title:
                        f.write(t.text +" ")
                    
                    for p in p_tags:
                        text = re.sub(r'\s{2,}', ' ', p.text)
                        f.write(text.strip() + '\n')
            break
        
    else:
        print("Failed to fetch the webpage.")

for i in range(46385, 60000, 1):
    url = "https://www.fortiguard.com/encyclopedia/virus/" + str(i+1)
    file = 'Crawl/results/fortinet_virus_' + str(i+1) + '.txt'
    
    print(i+1)
    crawl_website(url)


    