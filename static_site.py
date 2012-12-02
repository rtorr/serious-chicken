__author__ = 'rtorruellas'

import sys
import navigation
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    FREEZER_RELATIVE_URLS = True,
    FREEZER_BASE_URL = 'http://rtorr.github.com/serious-chicken',
)

pages = FlatPages(app)
freezer = Freezer(app)

nav = navigation.main_nav_method()

@app.route('/')
def index():
    return render_template('index.html', nav=nav)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page, nav=nav)

@app.route('/sitemap/')
def site_map():
    return render_template('map.html', pages=pages, nav=nav)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)