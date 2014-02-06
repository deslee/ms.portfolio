import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'entries'

app = Flask(__name__)
app.config.from_object(__name__)
entries = FlatPages(app)
freezer = Freezer(app)

@app.route('/', endpoint='index')
def index():
    results = [e for e in entries if e.meta.get('static', False) is False]
    return render_template('index.html', entries=results)

@app.route('/tagged/<string:tag>', endpoint='tagged')
def tag(tag):
    tagged = [p for p in entries if tag in p.meta.get('tags', [])]
    return render_template('tag.html', entries=tagged, tag=tag)

@app.route('/<path:path>/')
def page(path):
    entry = entries.get_or_404(path)
    if not entry.meta.get('title', False):
        print('aaa')
        entry.meta['title'] = path
    if entry.meta.get('static', False):
        return render_template('static.html', entry=entry)
    return render_template('entry.html', entry=entry)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(port=8000)