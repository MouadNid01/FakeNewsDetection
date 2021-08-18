import scrapy
# import os
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import json

class BreitbartLinksSpider(scrapy.Spider):
    name = 'BreitbartlinksSpider'
    
    def start_requests(self):
        base_url = 'https://www.breitbart.com/{}/page/{}'
        
        for i in ['politics', 'sports', 'world-news', 'tech', 'economy']:
           for j in range(100):
               url = base_url.format(i, j)
               yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath("//div[contains(@class, 'tC')]/h2/a")
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        # copying the links to .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/Breitbart_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
            
class NaturalLinksSpider(scrapy.Spider):
    name = 'NaturalLinksSpider'
    
    def start_requests(self):
        base_url = 'https://www.naturalnews.com/all-posts/page/{}'
        
        for j in range(500):
            url = base_url.format(j)
            yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath("//div[contains(@class, 'f-p-title')]/h2/a")
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        # copying the links to .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/NaturalNews_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

class WndLinksSpider(scrapy.Spider):
    name = 'WndLinksSpider'
    
    def start_requests(self):
        base_url = 'https://www.wnd.com/category/front-page/world/page/{}'
        
        for j in range(2000):
            url = base_url.format(j)
            yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath("/html/body/div[2]/div[2]/div/div/main/div/div[2]/article[1]/div/a")
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        # copying the links to .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/Wnd_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem.replace("https://www.wnd.com/", "")+'\n'
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)          

# class InfoWarsLinksSpider():
    
#     def __init__(self):
#         self.base_url = 'https://www.infowars.com/category/{}/'
#         self.chromrdriver = "./chromedriver"
#         os.environ["webdriver.chrome.driver"] = self.chromrdriver
    
#     def InitializeSpider(self):
#         for i in [11, 10, 8, 3, 14]:
#             url = self.base_url.format(i)
#             driver = webdriver.Chrome(self.chromrdriver)
#             file_path = 'InfoWars_temp'+str(i)+'.html'
            
#             driver.get(url)
#             time.sleep(1)
#             driver.find_element_by_xpath('//div[@class="css-1vj1npn"]/*[name()="svg"]/*[name()="path"]').click()
#             ScrollNumber = 50
#             for i in range(1,ScrollNumber):
#                 driver.execute_script("window.scrollTo(1, document.body.scrollHeight)")
#                 time.sleep(2)
#             file = open(file_path, 'w', encoding="utf-8")
#             file.write(driver.page_source)
#             file.close()
#             driver.close()
#         self.ExtractFromHtml()

#     def ExtractFromHtml(self):
#         tmp = 'InfoWars_temp{}.html'
#         for i in [11, 10, 8, 3, 14]:
#             tmp2 = tmp.format(i)
#             data = open(tmp2,'r', encoding="utf-8")
#             soup = BeautifulSoup(data, 'html.parser')
#             with open('./Links_temp/InfoWorld_links.txt', 'a') as infile:
#                 for link in soup.find_all('a', {'class': 'css-1xjmleq'}):
#                     temp = link.get('href')
#                     infile.write(temp+'\n')
#                     self.Extract_content(temp)
#             data.close()
#             # os.remove('./'+tmp2)
            
#     def Extract_content(self, link):
#         prefix = 'https://www.infowars.com'
#         driver2 = webdriver.Chrome(self.chromrdriver)
#         driver2.get(prefix+link)
#         try:
#             elem = WebDriverWait(driver2, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//div[@class="css-1vj1npn"]/*[name()="svg"]/*[name()="path"]')) #This is a dummy element
#             )
#             driver2.find_element_by_xpath('//div[@class="css-1vj1npn"]/*[name()="svg"]/*[name()="path"]').click()
#             soup = BeautifulSoup(driver2.page_source, 'html.parser')
#             content = []
#             heading = soup.find('h1', {'class': 'css-1f72nq5'}).text
#             div = soup.find('div', {'class': 'css-6lqlxw'})
#             for para in div.find_all('p'):
#                 p = para.text
#                 p = p.strip('/u')
#                 content.append(p)
#             tmp = '\n'.join(content)
#             tmp = tmp.split()
#             tmp = ' '.join(tmp[:351])
#             article={'title': heading, 'content': tmp}
#             with open('./Articles/InfoWars_articles.json', 'a') as file:
#                 out = json.dumps(article)
#                 file.write(out+'\n')
#         except:
#             pass
#         driver2.close()
           