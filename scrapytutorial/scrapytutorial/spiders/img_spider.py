import scrapy
import os.path

base_url = "http://img1.mm131.com/pic"
save_path = "images"


class QuotesSpider(scrapy.Spider):
    name = "images"

    def start_requests(self):
        package = 2800
        while package < 3000:
            urls = [base_url + "/" + str(package) + "/" + str(i) + ".jpg" for i in range(0, 100)]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
            package += 1

    def parse(self, response):
        if response.status == 404:
            pass
        package = response.url.split("/")[-2]
        img = response.url.split("/")[-1]
        filename = save_path + "/" + package + "/" + img

        if not os.path.exists(save_path + "/" + package):
            os.mkdir(save_path + "/" + package)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
