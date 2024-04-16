import requests
import csv
from bs4 import BeautifulSoup


# scraping logic...
page = requests.get('https://quotes.toscrape.com')
# print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

print("\n# ########################################################################\n")
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

print("\n#\n Extract data from the elements# ########################################################################\n")
quotes = []
quote_elements = soup.find_all('div', class_='quote')

for quote_element in quote_elements:
    # extract the text of the quote
    text = quote_element.find('span', class_='text').text
    # extract the author of the quote
    author = quote_element.find('small', class_='author').text

    # extract the tag <a> HTML elements related to the quote
    tag_elements = quote_element.select('.tags .tag')

    # store the list of tag strings in a list
    tags = []
    for tag_element in tag_elements:
        tags.append(tag_element.text)

    quotes.append(
        {
            'text': text,
            'author': author,
            'tags': ', '.join(tags) # merge the tags into a "A, B, ..., Z" string
        }
    )
for quote in quotes:
    print(quote)

print("\n#\n Implement the crawling logic # ########################################################################\n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# the URL of the home page of the target website
base_url = 'https://quotes.toscrape.com'

# retrieve the page and initializing soup...

# get the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # get the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parse the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    # scraping logic...

    # look for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')
    print("\n next_li_element: ", next_li_element)


print("\n#\n Implement the crawling logic # ########################################################################\n")

# scraping logic...

# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('quotes.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Text', 'Author', 'Tags'])

# writing each row of the CSV
for quote in quotes:
    writer.writerow(quote.values())

# terminating the operation and releasing the resources
csv_file.close()




