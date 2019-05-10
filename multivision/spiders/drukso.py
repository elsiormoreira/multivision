import scrapy


class DruksoSpider(scrapy.Spider):

    # name of the spider
    name = 'drukso'

    # list of allowed domains to be crawled
    allowed_domains = ['www.drukzo.nl.joao.hlop.nl/python.php']
    
    # list of urls where the spider will begin to crawl
    start_urls = ['https://www.drukzo.nl.joao.hlop.nl/python.php']
    

    def parse(self, response):

        # extract data from webpage using css selector
        tree = response.css("option::attr(value)").extract()
        
        # return multiple results from extratction
        row_data = zip(prodct)

        # transform extracted data into row wise
        for item in row_data:
        	# create a dictionary to store scraped info
        	scraped_info = {
        		'tree' : item[0]
        	}
        	# give scraped info to scrapy
        	yield scraped_info
        