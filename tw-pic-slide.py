import json
from flask import Flask, render_template, send_from_directory
import twitterparser

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/twitter/user/<username>')
def get_media_links(username):
    urls = twitterparser.get_media_links(username)
    return render_template('slide-ss.html', urls=urls)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/theme/<path:path>')
def send_theme(path):
    return send_from_directory('static/theme', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

if __name__ == '__main__':
    app.run(debug=True)