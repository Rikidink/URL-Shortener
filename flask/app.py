import string
import random
import validators
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Dictionary that will store the URLS
url_dict = {}

def gen_short_url():
    """Generates random 6 character alphanumerical string"""
    selection = string.ascii_letters + string.digits
    return ''.join(random.choices(selection, k=6))

# don't know if i'll use this
def is_valid_url(url):
    """True if input URL is valid otherwise false"""
    return validators.url(url)


# POST when they submit a URL to shorten, otherwise show main page
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # get long URL
        long_url = request.form['long_url']
        if not long_url.startswith("http://") and not long_url.startswith("https://"):
            long_url = "http://" + long_url

        # generate shortened URL
        short_url = gen_short_url()

        # add URL to dictionary with short URL as key
        url_dict[short_url] = long_url
        # print("DICT", url_dict)

        return render_template('index.html', short_url=request.base_url+short_url)
    
    # GET request
    return render_template('index.html')


# Route to redirect user
@app.route('/<short_url>')
def redirect_url(short_url):
    if short_url in url_dict:
        return redirect(url_dict[short_url])
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)