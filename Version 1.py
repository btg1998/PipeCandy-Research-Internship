import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class ScraperItem(scrapy.Item):
    # The source URL
    url_from = scrapy.Field()
    # The destination URL
    url_to = scrapy.Field()


class Spider(CrawlSpider):
    # The name of the spider
    name = "BTG"

    allowed_domains = ["fullenweider.com"]

    # The URLs to start with
    start_urls = ["https://www.fullenweider.com/"]

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract unique links
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            # Check whether the domain of the URL of the link is allowed
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = ScraperItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        # Return all the found items
        return items
