import scrapy
import json

# this file contains the spiders that uses the links extracted previously\
#     in order to get the article titles and their body.

class ReutersArticlesSpider(scrapy.Spider):
    name = 'ReutersArticlesSpider'
    
    def start_requests(self):
        with open("./Links_temp/Reuters_links.txt", 'r') as infile :
            # using the links stored in the file 'Reuters_links.txt' to extract the articles title and content 
            for line in infile:
                line.strip()
                yield scrapy.Request(url="https://www.reuters.com"+line)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("//h1[contains(@class, 'ArticleHeader-headline-NlAqj')]//text()").get()
        # if the first extraction xpath didn't work we'll use the second one.
        if article['title'] is None:
            article['title'] = response.xpath("//h1[contains(@class, 'Text__text___3eVx1j')]//text()").get()
            article['content'] = response.xpath("//div/p[contains(@class, 'Text__text___3eVx1j')]//text()").getall()
        else:
            article['content'] = response.xpath("//div/p[contains(@class, 'Paragraph-paragraph-2Bgue')]//text()").getall()
        
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/Reuters_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)

class NytimesArticlesSpider(scrapy.Spider):
    name = 'NytimesArticlesSpider'
    
    def start_requests(self):
        with open("./Links_temp/Nytimes_links.txt", 'r') as infile :
            # using the links stored in the file 'NyTimes_links.txt' to extract the articles title and content
            for line in infile:
                line.strip()
                yield scrapy.Request(url="https://www.nytimes.com"+line)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("//h1[contains(@data-testid, 'headline')]//text()").get()
        # we'll use getall() instead of get to extract all the <p> tags texts at once.
        article['content'] = response.xpath("//div/p[contains(@class, 'evys1bk0')]//text()").getall()
        
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/Nytimes_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)

class LaMapArticlesSpider(scrapy.Spider):
    name = 'LaMapArticlesSpider'
    
    def start_requests(self):
        with open("./Links_temp/LaMap_links.txt", 'r') as infile :
            # using the links stored in the file 'LaMap_links.txt' to extract the articles title and content
            for line in infile:
                line.strip()
                yield scrapy.Request(url="http://www.mapnews.ma"+line)
                
    def parse(self, response):
        article = {}
        article['title'] = response.xpath("//div[contains(@class, 'node-tpl-title')]/h2//text()").get()
        print(article['title'])
        # we'll use getall() instead of get to extract all the <p> tags texts at once.
        article['content'] = response.xpath("//div[contains(@class, 'node-tpl-corps')]/p//text()").getall()
        
        # converting the articles['content'] from list of strings to one string.
        tmp = '\n'.join(article['content'])
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/LaMap_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)

class TrtArticlesSpider(scrapy.Spider):
    name = 'TrtArticlesSpider'
    
    def start_requests(self):
        with open("./Links_temp/TRTWorld_links.txt", 'r') as infile :
            # using the links stored in the file 'TRTWorld_links.txt' to extract the articles title and content
            for line in infile:
                line.strip()
                yield scrapy.Request(url="https://www.trtworld.com"+line)
                
    def parse(self, response):
        # print(response.xpath("//div/h1[contains(@class, 'article-title')]//text()").get())
        article = {}
        article['title'] = response.xpath("//div/h1[contains(@class, 'article-title')]//text()").get()
        # we'll use getall() instead of get to extract all the <p> tags texts at once.
        # taking at first time only the article description
        article['content'] = response.xpath("//div[contains(@id, 't2')]/h3//text()").get()
        #extracting the article body
        tmp = response.xpath("//div[contains(@class, 'contentBox')]/p//text()").getall()
        # converting the tmp from list of strings to one string.
        tmp = '\n'.join(tmp)
        # concatenate the article description with the article body
        tmp = article['content']+'\n'+tmp
        tmp = tmp.split()
        article['content'] = ' '.join(tmp[:351])
        # writing the dictionnary to a json file.
        with open('./Articles/TRTWorld_articles.json', 'a') as json_file:
            if article['title'] is not None:
                out = json.dumps(article)
                json_file.write(out+"\n")
        for next_page in response.css('a.next'):
             yield response.follow(next_page, self.parse)
             
import scrapydo
scrapydo.setup()
scrapydo.run_spider(TrtArticlesSpider)