import requests
import csv
from bs4 import BeautifulSoup

URL = "https://bobdylan.fandom.com/wiki/Rough_and_Rowdy_Ways"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
role_text = "Not Found"
a_tag = soup.find('a', href="/wiki/Bob_Dylan")

if a_tag:
    li_element = a_tag.find_parent('li')  # Get the parent <li> element
    if li_element:
        role_text = li_element.text.strip()
        print(li_element.text.strip())  # Prints full text inside <li>
    else:
        print("No <li> parent found.")
else:
    print("No <a> tag found with href='/wiki/Bob_Dylan'.")
with open("dylaninst33.tsv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Artist", "Role"])
    writer.writerow(["Bob Dylan", role_text])