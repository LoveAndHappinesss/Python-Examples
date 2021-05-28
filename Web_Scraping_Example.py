'''
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')

two_star_titles = []

for n in range(1,51):

	scrape_url = base_url.format(n)
	res = requests.get(scrape_url)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	books = soup.select('.product_pod')

	for book in books:

		if len(books.select('.star-rating.Two')) != 0:

			book_title = book.select('a')[1]['title']
			two_star_titles.append(book_title)

print(two_star_titles)
'''

import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/{}/'
author_list = set()
page_valid = True
page = 1

while page_valid:

	scrape_url = base_url.format(page)
	res = requests.get(scrape_url)

	if "No quotes found!" in res.text:

		break

	else:

		soup = bs4.BeautifulSoup(res.text,'lxml')
		authors = soup.select('.author')

		for author in authors:

			author_list.add(author.text)

	page += 1

print('\n'.join(author_list))