import re
from bs4 import BeautifulSoup
import requests


def search_repos():
    search_text = input("Enter the search text for url : ")
    html_text = requests.get("https://github.com/vinta/awesome-python").text
    soup = BeautifulSoup(html_text, "lxml")
    all_tags = soup.find_all("li")
    search_result_counter = 0
    for tags in all_tags:
        hyperlink = tags.find_all('a', attrs={'href': re.compile("^https://")})
        for link in hyperlink:
            if search_text.lower() in link.get('href').lower():
                print(link.get('href'))
                search_result_counter += 1
            else:
                pass
    if search_result_counter == 0:
        print(f"search term {search_text} not in any of the links")


if __name__ == "__main__":
    search_repos()
