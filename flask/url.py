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