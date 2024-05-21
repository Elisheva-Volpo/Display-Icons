import urllib.request
from PIL import Image
import requests


url = "https://api.github.com/emojis"


def img(name,url):
    urllib.request.urlretrieve(
        url,
        name)
    img = Image.open(name)
    img.show()

def get_from_server():
    response = requests.get(url)
    if response.status_code == 200:
        emojis = response.json()
        print(type(emojis))
    else:
        print("Failed to retrieve data from API")

def print_all_icons():
    url = "https://api.github.com/emojis"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        icon_names = list(data.keys())
        print("List of icon names:")
        for icon_name in icon_names:
            print(icon_name)
    else:
        print("Failed to fetch icons. Status code:", response.status_code)

def search_icons_by_keyword(keyword):
    url = "https://api.github.com/emojis"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        matching_icons = [icon_name for icon_name in data.keys() if keyword.lower() in icon_name.lower()]
        if len(matching_icons)==1:
            img(matching_icons[0],data[matching_icons[0]])
        elif matching_icons:
            print("Matching icons for keyword '{}':".format(keyword))
            for index, icon_name in enumerate(matching_icons,start=1):
                print(f"{index}. {icon_name}")
            n=int(input("Please select the desired icon: "))
            img(matching_icons[n-1],data[matching_icons[n-1]])
        else:
            print("No icons found matching the keyword '{}'.".format(keyword))
    else:
        print("Failed to fetch icons. Status code:", response.status_code)



