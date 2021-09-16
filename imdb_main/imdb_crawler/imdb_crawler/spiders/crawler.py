import scrapy
from imdb_crawler.items import ImdbCrawlerItem

class imdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/search/keyword/?keywords=supernatural&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=bdc91cb7-0144-4906-b072-b45760c8aa67&pf_rd_r=YMV6XVFC7M2DSZVZ2V7Z&pf_rd_s=right-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_kw_16",
        "https://www.imdb.com/search/title/?genres=short,crime&genres=Documentary&explore=genres&ref_=adv_explore_rhs"]

    def parse(self, response):
        movie_item = ImdbCrawlerItem()

        for movie_info in response.css('div.lister-item-content'):
            movie_item['name'] = movie_info.css('a::text').get()
            movie_item['release_year'] = movie_info.css('span.lister-item-year.text-muted.unbold::text').get()
            movie_item['viewer_rating'] = movie_info.css('span.certificate::text').get()
            movie_item['runtime'] = movie_info.css('span.runtime::text').get()
            movie_item['genre'] = movie_info.css('span.genre::text').get()[1:-12]
            movie_item['stars'] = movie_info.css('strong::text').get()
            yield movie_item

        next_page = response.css('a.lister-page-next.next-page').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
