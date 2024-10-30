import requests
from bs4 import BeautifulSoup

page = 1
next_button = True

while next_button:

    website = requests.get('https://quotes.toscrape.com/page/' + str(page))  # returns a 'Response' object
    soup = BeautifulSoup(website.text, 'html.parser')
    next_button = soup.select_one('.next > a')

    # getting all the quotes, authors and tags from the website
    all_the_quotes = soup.select('.quote')
    for a_quote in all_the_quotes:
        text = a_quote.select_one('.text')
        author = a_quote.select_one('.author')
        tags = a_quote.select('.tag')

        print('Text: ', text.text)
        print('Author: ', author.text)
        print('Tags:'),
        for tag in tags:
            print(tag.text)

        print("==========================================")

    print("Scraped page - ", page)
    page += 1

