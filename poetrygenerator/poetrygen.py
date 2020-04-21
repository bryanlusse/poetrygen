from flask import render_template
from flask import Flask, request, url_for
from utils import generate_from_random, generate_from_seed
import sys


app = Flask(__name__)


# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # On form entry
    if request.method == 'POST':
        # Extract information
        seed = request.form.get("seed")
        length = int(request.form.get('length'))
        # Return to main page if user wants to make a new poem
        if "return" in request.form:
            return render_template('index.html')

        # Generate poem from a random sequence
        if seed == 'random':
            return render_template('random.html', input=generate_from_random(nr_words=length))

        # Generate poem from a seed sequence
        else:
            return render_template('seed.html', input=generate_from_seed(seed=seed, nr_words=length))


    # Send template information to index.html
    return render_template('index.html')


app.run(host='0.0.0.0', port=50000)
