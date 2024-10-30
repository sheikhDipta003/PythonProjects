import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')  # returns a 'Response' object
# print(website.text)     # returns html of the website

# create a beautifulsoup object
soup = BeautifulSoup(website.text, 'html.parser')

# getting the title of the website
title = soup.find('title')  # syntax: soup.find('<name of the html tag to be found>')
# It returns only the first element under the given tag in the website
# print(title.text)   # in order to get rid of the ending and closing tags

# getting the first link from the website
link = soup.find('a')
# print(link.text)

# getting an element using its className
firstQuote = soup.find(class_='text')  # class_ is used to distinguish it from the class keyword in python
# print(firstQuote.text)

# getting multiple elements at the same time
links = soup.find_all('a')
# print(links)
# print(links.text)   # error! trying to get text from a list
# for link in links:
#     print(link.text)

# getting all the quotes from the website
quotes = soup.find_all(class_='text')
# for quote in quotes:
#     print(quote.text)

login_link = soup.find(href='/login')
# print(login_link)

quote = soup.find(class_='quote')
quote_text = quote.find(class_='text')
quote_author = quote.find(class_='author')
# print("Quote: ", quote_text.text, "; author: ", quote_author.text)

# select one quote and one author using css selectors
quote_text = soup.select_one('.text')
quote_author = soup.select_one('.author')
# print("quote: ", quote_text.text, "; author: ", quote_author.text)

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

    print("\n")

