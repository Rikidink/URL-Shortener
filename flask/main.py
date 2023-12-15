import string
import random
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Dictionary that will store the URLS
url_dict = {}

def gen_short_url():
    """Generates random 6 character alphanumerical string"""
    selection = string.ascii_letters + string.digits
    return ''.join(random.choices(selection, k=6))


# POST when they submit a URL to shorten, otherwise show main page
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # get long URL
        long_url = request.form['long_url']

        # generate shortened URL
        short_url = gen_short_url()

        # add URL to dictionary with short URL as key
        url_dict[short_url] = long_url

        return render_template('index.html', short_url=short_url)
    
    # GET request
    return render_template('index.html')