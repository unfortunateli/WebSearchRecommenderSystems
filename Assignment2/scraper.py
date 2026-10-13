#-------------------------------------------------------------------------
# AUTHOR: Nathan Li
# FILENAME: scraper.py
# SPECIFICATION: A simple web scraper to crawl and extract information from a website
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 30 mins
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]
seen = {seed}


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    current_url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    h1_tag = soup.find("h1")
    if h1_tag:
        print(h1_tag.get_text(strip=True))

    # Extracting and processing hyperlinks
    links = soup.find_all("a", href=True)

    for link in links:
        absolute_url = requests.compat.urljoin(
            current_url,
            link["href"]
        )

        if absolute_url.startswith(seed) and absolute_url not in seen:
            seen.add(absolute_url)
            frontier.append(absolute_url)


# Printing all URLs in seen
print("All URLs in seen:")
for url in seen:
    print(url)