import requests
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/Dariush_Mehrjui"
headers = {
    "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) Applewebkit/537.36 "
                  "(KHTL, like Geko) chrome/117.0 Safari/537.36"
}

my_string_web_page = requests.get(url, headers=headers).text

my_parsed_page = bs(my_string_web_page, "html.parser")

heading = my_parsed_page.find(id="Filmography")

# print("heading", heading)


ul_element = heading.find_parent().findNextSibling('ul')
li_elements = ul_element.find_all("li")

# print("ul_element", ul_element)
# print("li_elements", li_elements)

print(li_elements[0])


for movie_name in li_elements:
    # print("Movie name:", movie_name.get_text())
    # print("Link", movie_name)
    pass