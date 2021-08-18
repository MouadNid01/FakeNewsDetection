import scrapy
import json
import time

# this file contains the spiders that uses the links extracted previously\
#     in order to get the article titles and their body.

class BreitbartArticlesSpider(scrapy.Spider):
    name = 'BreitbartArticlesSpider'
    
    def start_requests(self):
        url_prefix = 'https://www.breitbart.com'
        with open("./Links_temp/Breitbart_links.txt", 'r') as infile :
            # using the links stored in the file 'Reuters_links.txt' to extract the articles title and content 
            for line in infile:
                line.strip()
                url = url_prefix+line
                yield scrapy.Request(url=url)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("//h1//text()").get()
        # if the first extraction xpath didn't work we'll use the second one.
        article['content'] = response.xpath("//div[contains(@class, 'entry-content')]/p//text()").getall()
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/Breitbart_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)
             
class NaturalArticlesSpider(scrapy.Spider):
    name = 'NaturalArticlesSpider'
    
    def start_requests(self):
        url_prefix = 'https://www.naturalnews.com/'
        with open("./Links_temp/NaturalNews_links.txt", 'r') as infile :
            # using the links stored in the file 'Reuters_links.txt' to extract the articles title and content 
            for line in infile:
                line.strip()
                url = url_prefix+line
                yield scrapy.Request(url=url)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("//div[contains(@id, 'Headline')]/h1//text()").get()
        # if the first extraction xpath didn't work we'll use the second one.
        article['content'] = response.xpath("//div[contains(@class, 'entry-content')]/p//text()").getall()
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/NaturalNews_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)

class WndArticlesSpider(scrapy.Spider):
    name = 'WndArticlesSpider'
    
    def start_requests(self):
        url_prefix = 'https://www.wnd.com/'
        with open("./Links_temp/Wnd_links.txt", 'r') as infile :
            # using the links stored in the file 'Reuters_links.txt' to extract the articles title and content 
            for line in infile:
                line.strip()
                url = url_prefix+line
                yield scrapy.Request(url=url)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("/html/body/div[2]/div[2]/div/div/main/article/header/h1//text()").get()
        # if the first extraction xpath didn't work we'll use the second one.
        article['content'] = response.xpath("/html/body/div[2]/div[2]/div/div/main/article/div[2]/p//text()").getall()
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/Wnd_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)

# import scrapydo
# scrapydo.setup()
# scrapydo.run_spider()
