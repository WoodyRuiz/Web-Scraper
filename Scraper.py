import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import re

# Here, we're just importing both Beautiful Soup and the Requests library


# page_link = 'https://www.pokemon.com/us/pokedex/bulbasaur'
# this is the url that we've already determined is safe and legal to scrape from.

# page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library

# page_content = BeautifulSoup(page_response.content, "html.parser")
# we use the html parser to parse the url content and store it in a variable.


# height = page_content.findAll("span", class_="attribute-value")[0].text
#
# weight = page_content.findAll("span", class_="attribute-value")[1].text
#
# abilities = page_content.find("ul", class_="attribute-list")
#
# ability1 = abilities.findAll("span", class_="attribute-value")[0].text
#
# print(ability1)
#
# try:
#     ability2 = abilities.findAll("span", class_="attribute-value")[1].text
# except:
#     ability2 = "None"
#
# print(ability2)
#
# ability1 = page_content.findAll("span", class_="attribute-value")[4].text
#
# try:
#     ability2 = page_content.findAll("span", class_="attribute-value")[5].text
# except:
#     ability2 = "None"
#
# bio = page_content.find("p", class_="version-y").text.strip()
# bio = bio.replace('\n', " ")
#
# type1 = page_content.findAll("li", class_=re.compile('background-color-*'))[0].text.strip()
#
# try:
#     type2 = page_content.findAll("li", class_=re.compile('background-color-*'))[1].text.strip()
# except:
#     type2 = "None"
#
# title = page_content.findAll("div", class_="pokedex-pokemon-pagination-title")
#
# name = title[0].find("div").text.split()[0]
#
# number = title[0].find("div").text.split()[1]
# number = re.sub('[#]', '', number)
#
# imgSrc = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + number + ".png"
#
# number = number.lstrip('0')
#
# urllib.urlretrieve(imgSrc,"Images/" + number + ".png")
#
#
# pokemon = number + "\t" + name + "\t" + height + "\t" + weight + "\t" + bio + "\t" + ability1 + "\t" + ability2 + "\t" + type1 + "\t" + type2

# img = page_content.findAll("div", class_="profile-images")
#
# print(img)
#
# print(<img class="active" src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png" alt="Bulbasaur">)
# imgUrl = img.a['src'].split("imgurl=")[0]
# urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))

# print(pokemon)

###########################CODE WORKS UNDER HERE#######################################################
f = open("pokemon_names.txt", "r")
for i in f:
    page_link = 'https://www.pokemon.com/us/pokedex/' + i.strip()
    # This is the url that we've already determined is safe and legal to scrape from.

    page_response = requests.get(page_link, timeout=5)
    # Here, we fetch the content from the url, using the requests library

    page_content = BeautifulSoup(page_response.content, "html.parser")
    # Ee use the html parser to parse the url content and store it in a variable.

    # Get the height
    try:
        height = page_content.findAll("span", class_="attribute-value")[0].text
    except:
        height = "0"

    # Get the weight
    try:
        weight = page_content.findAll("span", class_="attribute-value")[1].text
    except:
        weight = "0"

    # Get Ability 1
    abilities = page_content.find("ul", class_="attribute-list")
    try:
        ability1 = abilities.findAll("span", class_="attribute-value")[0].text
    except:
        ability1 = "None"

    # Get Ability 2
    try:
        ability2 = abilities.findAll("span", class_="attribute-value")[1].text
    except:
        ability2 = "None"

    # Get the Bio
    try:
        bio = page_content.find("p", class_="version-y").text.strip()
        bio = bio.replace('\n', " ")
    except:
        bio = ""

    # Get the First Type
    try:
        type1 = page_content.findAll("li", class_=re.compile('background-color-*'))[0].text.strip()
    except:
        type1 = "None"

    # Get the Second Type
    try:
        type2 = page_content.findAll("li", class_=re.compile('background-color-*'))[1].text.strip()
    except:
        type2 = "None"

    title = page_content.findAll("div", class_="pokedex-pokemon-pagination-title")

    try:
        try:
            # Get the Name
            name = title[0].find("div").text.split()[0]
            name += title[0].find("div").text.split()[1]

            # Get the Number
            number = title[0].find("div").text.split()[2]
            number = re.sub('[#]', '', number)

            # Get the image
            imgSrc = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + number + ".png"

            # Strip the number
            number = number.lstrip('0')

            # Download the Image
            urllib.urlretrieve(imgSrc, "Images/" + number + ".png")
        except:

            name = title[0].find("div").text.split()[0]

            number = title[0].find("div").text.split()[1]
            number = re.sub('[#]', '', number)
            imgSrc = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + number + ".png"
            number = number.lstrip('0')
            urllib.urlretrieve(imgSrc, "Images/" + number + ".png")
    except:
        name = ""
        number = ""

    # Format the pokemon details
    pokemon = number + "\t" + name + "\t" + height + "\t" + weight + "\t" + bio + "\t" + ability1 + "\t" + ability2 + "\t" + type1 + "\t" + type2 + "\n"

    pokemon = pokemon.encode('utf-8')
    output = open("pokemon.txt", "a+")
    output.write(pokemon)

f.close()
output.close()
