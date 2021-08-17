import scrapy
import datetime

 # this file takes care of extracting articles links from news websites \
 #    the websites used in this step are Reuters, NyTimes, LaMap

class ReutersLinksSpider(scrapy.Spider):
    name = 'ReuterslinksSpider'
    
    def start_requests(self):
        base_url = 'https://www.reuters.com/news/archive?page={}'
        # for changing pages
        # extracting article links from 385 page.
        for i in range(1, 500):
            url = base_url.format(i)
            yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath("//div/a[starts-with(@href,'/article/')]")
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        # copying the links to .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/Reuters_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
            
class NytimesLinksSpider(scrapy.Spider):
    name = 'NytimeslinksSpider'
    
    def start_requests(self):
        # extracting the articles of a 100 day.
        base_url = 'https://www.nytimes.com/sitemap/{}/{}/{}/'
        self.date = datetime.date.today()
        for i in range(150):
            day = self.date.day
            month = self.date.month
            if day // 10 == 0:
                day = "0"+ str(day)
            if month // 10 == 0:
                month = "0"+ str(month)
            url = base_url.format(self.date.year, month, day)
            self.date -= datetime.timedelta(days=1)
            yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        src = response.url
        temp = src.replace("/sitemap", "")
        # ignoring articles from other domains than sports, politicts, health... 
        for keyword in ['world/', 'sports/', 'us/politics/', 'health/']:
            articles = response.xpath('//li/a[starts-with(@href,"'+temp+keyword+'")]')
            if articles is not None:
                break

        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        
        # writing the links into a .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/Nytimes_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                tmp = tmp.replace("https://www.nytimes.com", "")
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

class LaMapLinksSpider(scrapy.Spider):
    name = 'LaMapLinksSpider'
    
    def start_requests(self):
        base_url = 'http://www.mapnews.ma/en/actualites/{}?page={}'
        # the extracted articles belongs to sport, social and economie domains.
        for i in ['social', 'sport', 'economie']:
           for j in range(100):
               url = base_url.format(i, j)
               yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath('//div[contains(@class, "actualites-lire-la-suite")] \
                                  /span/a')
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        
        # writing the links into a .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/LaMap_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

class TrtLinksSpider(scrapy.Spider):
    name = 'TrtLinksSpider'
    
    def start_requests(self):
        base_url = 'https://www.trtworld.com/{}?page={}'
        # the extracted articles belongs to sport, social and economie domains.
        for i in ['business', 'life', 'sport']:
           for j in range(100):
               url = base_url.format(i, j)
               yield scrapy.Request(url=url)

    def parse(self, response):
        #extracting the links of the articles
        articles = response.xpath('//div/a[contains(@class, "gtm-topic-latest-article")]')
        article_links = []
        for article in articles:
            link = article.xpath("@href").extract_first()
            # grouping all the links into a list of unique values.
            if link not in article_links:
                article_links.append(link)
        
        # writing the links into a .txt file that works like an intermediary between 
        # the links spider and the article spider.
        with open('./Links_temp/TRTWorld_links.txt', 'a') as infile:
            for elem in article_links:
                tmp = elem+"\n"
                infile.write(tmp)
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)