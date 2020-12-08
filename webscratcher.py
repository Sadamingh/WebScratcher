import requests
import time
import random
from bs4 import BeautifulSoup
import sys, os
from tqdm import tqdm

def fetch(url, delay=(1,3)):
    """
    Simulate human random clicking x..y seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        response = requests.get(url, headers={'User-Agent': "Resistance is futile"})
    except ValueError as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    page = response.text
    soup = BeautifulSoup(page, "html.parser")

    return page, soup


def parse(soup, tagname, classname=None):
	"""
	The prase function will grab all the links based on a 
	certain class name and a certain tag of this element 
	in the HTML page.
	"""
    links = []
    for link in soup.find_all(tagname, class_=classname):
        links.append(link['href'])

    return links


def crawl(links):
	"""
	The crawl function walk though all the links in the list
	and then 
	"""
	for link in tqdm(links, ascii=True, desc='Crawling: '):
		_, soup = fetch(url)

		# do something here

	return 


_, soup = fetch(url)
crawl(parse(soup, tagname, classname))
