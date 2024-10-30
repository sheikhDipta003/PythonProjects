import requests
from bs4 import BeautifulSoup

website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text, 'html.parser')

links = soup.select('.topic-list .md-crosslink')
print(links)

for link in links[:5]:
    try:
        website = requests.get(link.attrs['href'])
        soup = BeautifulSoup(website.text, 'html.parser')

        name = soup.select_one('h1').text
        short_description = soup.select_one('.topic-identifier').text
        details = soup.select_one('.topic-paragraph').text

        try:
            image = soup.select_one('.fact-box-picture img').attrs['src']
        except AttributeError as error:
            image = None  # If there is no image, set it to None

        birth = soup.select('.fact-box-details dd')[0].get_text('|').split('|')[0]
        death = soup.select('.fact-box-details dd')[1].get_text('|').split('|')[0]
        subjects = ""

        try:
            subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select('ul li')
            for item in subjects_of_study:
                subjects += item.text.strip() + ", "
        except AttributeError as error:
            subjects = None

        print(name)
        print(short_description)
        print(details)
        print(image)
        print(birth)
        print(death)
        print(subjects)
    except:
        print("Something went wrong!")
