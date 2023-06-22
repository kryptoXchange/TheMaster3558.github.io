from flask import Flask, render_template_string, send_from_directory, send_file
from flask_frozen import Freezer


app = Flask(__name__)


with open('index.html') as f:
    index_html = f.read()


@app.route('/')
def home():
    return render_template_string(index_html)


@app.route('/maps.png')
def maps():
    return send_file('maps.png')


@app.route('/pencilPic.jfif')
def pencil():
    return send_file('pencilPic.jfif')


@app.route('/_next/static/<path:path>')
def serve_next_files(path):
    return send_from_directory('_next/static/', path)


freezer = Freezer(app)


if __name__ == '__main__':
    freezer.freeze()
