import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(website.text, 'html.parser')

first_table = soup.select_one('.wikitable')
table_rows = first_table.select('tr')[1:-1]   # to get rid of the table heading and the footer

csv_data = [['rank', 'name', 'population', 'percentage', 'date', 'source']]

for row in table_rows:
    rank = row.find('th').text.strip()
    details = row.find_all('td')

    info = str(rank) + "\t"
    for d in details:
        d = d.text.strip().split('[')[0]    # To discard the ending square brackets containing reference numbers
        info += str(d) + "\t"

    csv_data.append(info.split('\t')[0:6])  # [0:6] --> to avoid the unnecessary blank string

    # print(info)
print(csv_data)

with open('countries_population.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
