import scrapy
from imdb_crawler.items import ImdbCrawlerItem

class imdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/search/title/?genres=thriller&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=0KXYBFENHD1RD0R7JBY6&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_19",
        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=musical&sort=user_rating,desc&start=151&ref_=adv_nxt"]

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
