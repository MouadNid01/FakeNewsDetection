import RealLinks_scrapping
import RealArticles_scraping
import FakeLinks_scraping
import FakeArticles_scraping
from multiprocessing import Process
# usig scrapydo library to avoid scrapy errors (Not restartable issues).
import scrapydo
scrapydo.setup()

def scrape(LinksSpider, ArticleSpider):
    scrapydo.run_spider(LinksSpider)
    scrapydo.run_spider(ArticleSpider)

def InitializeScraping():
    a1 = Process(target = scrape, args=(RealLinks_scrapping.ReutersLinksSpider, \
                                        RealArticles_scraping.ReutersArticlesSpider,))
    a2 = Process(target = scrape, args=(RealLinks_scrapping.NytimesLinksSpider, \
                                        RealArticles_scraping.NytimesArticlesSpider,))
    a3 = Process(target = scrape, args=(RealLinks_scrapping.LaMapLinksSpider, \
                                        RealArticles_scraping.LaMapArticlesSpider,))
    a4 = Process(target = scrape, args=(RealLinks_scrapping.TrtLinksSpider, \
                                                      RealArticles_scraping.TrtArticlesSpider,))
    
    
    b1 = Process(target = scrape, args=(FakeLinks_scraping.BreitbartLinksSpider, \
                                                      FakeArticles_scraping.BreitbartArticlesSpider,))
    b2 = Process(target = scrape, args=(FakeLinks_scraping.NaturalLinksSpider, \
                                                      FakeArticles_scraping.NaturalArticlesSpider,))
    b3 = Process(target = scrape, args=(FakeLinks_scraping.WndLinksSpider, \
                                                      FakeArticles_scraping.WndArticlesSpider,))
    
    return [a1, a2, a3, a4, b1, b2, b3]

InitializeScraping()