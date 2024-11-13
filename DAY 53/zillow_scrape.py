from bs4 import BeautifulSoup
import requests


class Scrape_listings:
    def __init__(self):
        headers = requests.utils.default_headers()
        headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            }
        )
        response = requests.get(
            "https://www.zillow.com/san-francisco-ca/rentals/2_p/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.98909178903854%2C%22south%22%3A37.56087204301267%2C%22east%22%3A-122.23866549853516%2C%22west%22%3A-122.62799350146484%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%7D%2C%22mp%22%3A%7B%22min%22%3Anull%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22schm%22%3A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22schu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D",
            headers=headers,
        )
        self.html_doc = response.content
        self.soup = BeautifulSoup(self.html_doc, "html.parser")
        self.prices = []
        self.addresses = []
        self.links = []
        self.get_prices()
        self.get_addresses()
        self.get_links()

    def get_prices(self):
        prices = self.soup.select('span[data-test="property-card-price"]')
        for price in prices:
            price_text = price.text.split(" ")[0]
            self.prices.append(price_text)

    def get_addresses(self):
        addresses = self.soup.select('address[data-test="property-card-addr"]')
        for address in addresses:
            address_text = address.text
            self.addresses.append(address_text)

    def get_links(self):
        links = self.soup.select(".property-card-link")
        for link in links:
            link_text = link.get("href")
            if link_text.startswith("/"):
                link_text = "https://www.zillow.com" + link_text
            self.links.append(link_text)
