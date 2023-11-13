# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Import the CSV library
import csv

# Open a new CSV file. Choose any desired name for the file.
file = open('scraped_quotes.csv', 'w')

# Create a variable for writing to the CSV
writer = csv.writer(file)

# Create the header row of the CSV
writer.writerow(['Quote', 'Author'])

# Request the webpage and store it as a variable
page_to_scrape = requests.get("http://quotes.toscrape.com")

# Use BeautifulSoup to parse the HTML and store it as a variable
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# Find all the items on the page with a class attribute of 'text'
# and store the list as a variable
quotes = soup.findAll('span', attrs={'class': 'text'})

# Find all the items on the page with a class attribute of 'author'
# and store the list as a variable
authors = soup.findAll('small', attrs={"class": "author"})

# Loop through both lists using the 'zip' function
# Print and format the results
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    # Write each item as a new row in the CSV
    writer.writerow([quote.text, author.text])

# Close the CSV file
file.close()
