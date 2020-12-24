import requests
from bs4 import BeautifulSoup
import json
def magic_stories_links(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    find = soup.findAll(class_="teaser-image")
    empty_magic_fantasy =[]
    for i in find:
        for link in i.find_all('a', href=True):
            empty_magic_fantasy.append(link['href'])
    magic_fantasy_list = []
    magic_audio = []
    json_arr = []
    for x in empty_magic_fantasy:
        response = requests.get(x)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        results = soup.findAll(class_='field-items')
        for x in results:
            magic_fantasy_list.append(x.text)
            result2 = soup.findAll('video')
            for i in result2:
                video_src = i.findAll('source')[0]
                magic_audio.append(video_src['src'])
            for j in magic_audio:
                dictionary = {"title": title, "pargraph": x.text, "audio": j}
            json_arr.append(dictionary)
    json_object = json.dumps(json_arr, indent=4)
    with open('../json/magic.json', 'w') as f:
        f.write(json_object)
def funny_stories_links(URL2):
    page = requests.get(URL2)
    soup = BeautifulSoup(page.content, 'html.parser')
    find = soup.findAll(class_="teaser-image")
    empty_funny =[]
    for i in find:
         for link in i.find_all('a', href=True):
             empty_funny.append(link['href'])
    funny_list = []
    funny_audio = []
    json_arr = []
    for x in empty_funny:
        response = requests.get(x)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        results = soup.findAll(class_='field-items')
        for x in results:
            funny_list.append(x.text)
            result2 = soup.findAll('video')
            for i in result2:
                video_src = i.findAll('source')[0]
                funny_audio.append(video_src['src'])
            for j in funny_audio:
                dictionary = {"title": title, "pargraph": x.text, "audio": j}
            json_arr.append(dictionary)
    json_object = json.dumps(json_arr, indent=4)
    with open('../json/funny.json', 'w') as f:
        f.write(json_object)
#
def big_concept_stories_links(URL3):
    page = requests.get(URL3)
    soup = BeautifulSoup(page.content, 'html.parser')
    find = soup.findAll(class_="teaser-image")
    empty_big_concept =[]
    for i in find:
         for link in i.find_all('a', href=True):
             empty_big_concept.append(link['href'])
    big_concept_list = []
    big_concept_audio = []
    json_arr = []
    for x in empty_big_concept:
        response = requests.get(x)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        results = soup.findAll(class_='field-items')
        for x in results:
            big_concept_list.append(x.text)
            result2 = soup.findAll('video')
            for i in result2:
                video_src = i.findAll('source')[0]
                big_concept_audio.append(video_src['src'])
            for j in big_concept_audio:
                dictionary = {"title":title ,"pargraph": x.text ,"audio": j}
            json_arr.append(dictionary)
    json_object = json.dumps(json_arr, indent=4)
    with open('../json/big_concept.json', 'w') as f:
        f.write(json_object)
def top10_stories_links(URL4):
    page = requests.get(URL4)
    soup = BeautifulSoup(page.content, 'html.parser')
    find = soup.findAll(class_="teaser-image")
    empty_top10 = []
    for i in find:
         for link in i.find_all('a', href=True):
            empty_top10.append(link['href'])
    top10_list = []
    top10_audio = []
    json_arr = []
    for x in empty_top10:
        response = requests.get(x)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        results = soup.findAll(class_='field-items')
        for x in results:
            top10_list.append(x.text)
            result2 = soup.findAll('video')
            for i in result2:
                video_src = i.findAll('source')[0]
                top10_audio.append(video_src['src'])
            for j in top10_audio:
                dictionary = {"title": title, "pargraph": x.text, "audio": j}
            json_arr.append(dictionary)
    json_object = json.dumps(json_arr, indent=4)
    with open('../json/top10.json', 'w') as f:
        f.write(json_object)
if __name__ == '__main__':
    URL ="https://freestoriesforkids.com/stories-collections/magic-and-fantasy?page=1"
    URL2 ="https://freestoriesforkids.com/stories-collections/funny-stories-and-tales"
    URL3 ="https://freestoriesforkids.com/content/insertedviews/our-best-ranked-stories-children?page=15"
    URL4 ="https://freestoriesforkids.com/content/insertedviews/our-best-ranked-stories-children?page=16"
    magic_stories_links(URL)
    funny_stories_links(URL2)
    big_concept_stories_links(URL3)
    top10_stories_links(URL4)