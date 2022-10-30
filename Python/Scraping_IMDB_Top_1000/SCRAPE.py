import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
# base_url = requests.get(
#     'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=001&ref_=adv_nxt')
# c = base_url.content
# # print(c)

# soup = BeautifulSoup(base_url.text, 'html.parser')

# all = soup.find("div", {"class": "lister-item mode-advanced"})
# print(all.find("h3", {"class": "lister-item-header"}
#                ).find("a").get_text(strip=True))
# # # print(all)
# print(all.find("h3", {"class": "lister-item-header"}).find("span",
#                                                            "lister-item-year text-muted unbold").get_text(strip=True))
# c=all.find_all("p", {"class": "text-muted"})
# print(c)
# print(c[1].get_text(strip=True))
# print(c[0].find("span", "certificate").get_text(strip=True))
# print(c[0].find("span", "runtime").get_text(strip=True))
# print(c[0].find("span", "genre").get_text(strip=True))
# print(all.find("p", {"class": ""}).get_text(strip=True))
# a =all.find("p", {"class": "sort-num_votes-visible"})
# print(a)
# b=a.find_all("span",{"name": "nv"})
# print(b[0].text)
# print(b[1].text)
# print(all.find("div", {"class": "inline-block ratings-imdb-rating"}).get_text(strip=True))
# print(all.find("div", {"class": "inline-block ratings-metascore"}).find("span").get_text(strip=True))

l = []
for i in range(10):
    # print("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+i+"01&ref_=adv_nxt")
    web_url = requests.get(
        "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+f"{i}"+"01&ref_=adv_nxt").text
    soup = BeautifulSoup(web_url, 'html.parser')
    all = soup.find_all("div", {"class": "lister-item mode-advanced"})
    for item in all:
        d = {}
        try:
            d["TITLE"] = (item.find(
                "h3", {"class": "lister-item-header"}).find("a").get_text(strip=True))
        except:
            d["TITLE"] = "Not mentioned"
        try:
            d["RELEASE YEAR"] = re.sub("[^0-9]", "", item.find("h3", {"class": "lister-item-header"}).find(
                "span", "lister-item-year text-muted unbold").get_text(strip=True).replace('(', '').replace(')', ''))
        except:
            d["RELEASE YEAR"] = "Not mentioned"
        c = item.find_all("p", {"class": "text-muted"})
        try:
            d["CERTIFICATE"] = c[0].find(
                "span", "certificate").get_text(strip=True)
        except:
            d["CERTIFICATE"] = "Not mentioned"
        try:
            d["RUNTIME"] = c[0].find("span", "runtime").get_text(strip=True)
        except:
            d["RUNTIME"] = "Not mentioned"
        try:
            d["GENRE"] = c[0].find("span", "genre").get_text(strip=True)
        except:
            d["GENRE"] = "Not mentioned"
        try:
            d["IMDB RATING"] = item.find(
                "div", {"class": "inline-block ratings-imdb-rating"}).get_text(strip=True)
        except:
            d["IMDB RATING"] = "Not mentioned"
        try:
            d["METASCORE"] = item.find(
                "div", {"class": "inline-block ratings-metascore"}).find("span").get_text(strip=True)
        except:
            d["METASCORE"] = "Not mentioned"
        try:
            d["DESCRIPTION"] = c[1].get_text(strip=True)
        except:
            d["DESCRIPTION"] = "Not mentioned"
        try:
            d["FILM CREW"] = item.find("p", {"class": ""}).get_text(strip=True)
        except:
            d["FILM CREW"] = "Not mentioned"
        a = item.find("p", {"class": "sort-num_votes-visible"}
                      ).find_all("span", {"name": "nv"})
        try:
            d["VOTES"] = a[0].get_text(strip=True)
        except:
            d["VOTES"] = "Not mentioned"
        try:
            d["GROSS"] = a[1].get_text(strip=True)
        except:
            d["GROSS"] = "Not mentioned"
        l.append(d)
df = pd.DataFrame(l)
df.to_csv("Output.csv")
