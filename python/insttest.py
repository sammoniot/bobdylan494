import requests
import csv
from bs4 import BeautifulSoup

# URL of the album page
URL = "https://bobdylan.fandom.com/wiki/Rough_and_Rowdy_Ways"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

# Find the "Personnel" section by locating the <h2> with id="Personnel"
personnel_header = soup.find('span', {'id': 'Personnel'})

# Initialize an empty list for roles
roles = []

if personnel_header:
    # Find the next <ul> after the "Personnel" heading
    ul_element = personnel_header.find_parent().find_next_sibling("ul")

    if ul_element:
        # Find all <li> elements inside that <ul>
        for li in ul_element.find_all('li'):
            roles.append(li.text.strip())  # Extract and store text from <li>
    else:
        print("No <ul> found under Personnel section.")
else:
    print("Personnel section not found.")

# Save to TSV file
with open("dylaninst33.tsv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Artist", "Role"])  # Header row
    for role in roles:
        writer.writerow(["Bob Dylan", role])  # Write each role in a new row

print("Data successfully saved to dylaninst3.tsv")
