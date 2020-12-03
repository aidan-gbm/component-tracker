from bs4 import BeautifulSoup
import requests
import datetime
import csv
import os

class Tracker():

    def __init__(self):
        self.components = {
            'Ryzen 5 3400G': 'https://www.newegg.com/amd-ryzen-5-3400g/p/N82E16819113570',
            'Ryzen 5 2600': 'https://www.newegg.com/amd-ryzen-5-2600/p/N82E16819113496',
            'Ryzen 5 2600X': 'https://www.newegg.com/amd-ryzen-5-2600x/p/N82E16819113497'
        }
    
    def getInfo(self, name, url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        price = soup.findAll('div', {'class':'product-price'})[0].findAll('li', {'class':'price-current'})[0].text
        vendor = list(soup.findAll('div', {'class':'product-seller'})[0].children)[1].text
        return (vendor, float(price.split('$')[1]))

    def update(self):
        results = {}
        date = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        for name, url in self.components.items():
            (vendor, price) = self.getInfo(name, url)
            results[name] = {'date': date, 'vendor': vendor, 'price': price}

        for n,d in results.items():
            fname = './data/' + n.replace(' ', '_') + '.csv'
            file_exists = os.path.isfile(fname)
            with open(fname, 'a+', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=d.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(d)
