import requests
from bs4 import BeautifulSoup


# scraping logic...
page = requests.get('https://quotes.toscrape.com')
# print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

# get all <h1> elements
# on the page
h1_elements = soup.find_all('h1')
print("h1_elements : ", h1_elements)

# get the element with id="main-title"
main_title_element = soup.find(id='main-title')
print("main_title_element : ", main_title_element)

# find the footer element
# based on the text it contains
footer_element = soup.find(string={'Powered by WordPress'})
print("footer_element : ", footer_element)

# find the email input element
# through its "name" attribute
email_element = soup.find(attrs={'name': 'email'})
print("email_element : ", email_element)

# find all the centered elements
# on the page
centered_element = soup.find_all(class_='text-center')
print("centered_element : ", centered_element)

# get all "li" elements
# in the ".navbar" element
print(soup.select('.navbar > li'))

