from flask import Flask, render_template, request, redirect, url_for, send_file
import requests
from PIL import Image
import urllib.request
import os

app = Flask(__name__)

GITHUB_EMOJIS_URL = "https://api.github.com/emojis"
IMAGES_FOLDER = 'static/images'

# Ensure the images folder exists
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

def img(name, url):
    image_path = os.path.join(IMAGES_FOLDER, name)
    urllib.request.urlretrieve(url, image_path)
    return image_path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/icons')
def print_all_icons():
    response = requests.get(GITHUB_EMOJIS_URL)
    if response.status_code == 200:
        data = response.json()
        icon_names = list(data.keys())
        return render_template('icons.html', icons=icon_names)
    else:
        return "Failed to fetch icons.", 500

@app.route('/search', methods=['GET', 'POST'])
def search_icons_by_keyword():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        response = requests.get(GITHUB_EMOJIS_URL)
        if response.status_code == 200:
            data = response.json()
            matching_icons = [icon_name for icon_name in data.keys() if keyword.lower() in icon_name.lower()]
            if matching_icons:
                return render_template('search_results.html', keyword=keyword, icons=matching_icons, data=data)
            else:
                return "No icons found matching the keyword '{}'.".format(keyword), 404
        else:
            return "Failed to fetch icons.", 500
    return render_template('search.html')

@app.route('/show_icon/<icon_name>')
def show_icon(icon_name):
    response = requests.get(GITHUB_EMOJIS_URL)
    if response.status_code == 200:
        data = response.json()
        if icon_name in data:
            image_path = img(icon_name + '.png', data[icon_name])
            return send_file(image_path, mimetype='image/png')
        else:
            return "Icon not found.", 404
    else:
        return "Failed to fetch icons.", 500

if __name__ == '__main__':
    app.run(debug=True)
