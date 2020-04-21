import re
from fastai.basic_train import load_learner
import sys


def generate_from_random(nr_words):
    model = load_learner("", "poetrygenerator/poetry_model2.pkl")
    seed = "xxbos"
    sequence = model.predict(seed, n_words=nr_words, temperature=0.8)
    improved_sequence = sequence.replace("xxbos", "").strip()
    html_sequence = improved_sequence.replace("\n", '<br>')

    seed_html = ''
    seed_html = addContent(seed_html, html_sequence)

    return f"{seed_html}"


def generate_from_seed(seed, nr_words):
    model = load_learner("", "poetrygenerator/poetry_model2.pkl")
    sequence = model.predict(seed, n_words=nr_words, temperature=0.8)
    improved_sequence = sequence.replace("xxbos", "").strip()
    html_sequence = improved_sequence.replace("\n", '<br>')

    seed_html = ''
    seed_html = addContent(seed_html, html_sequence)

    return f"{seed_html}"


def addContent(old_html, raw_html):
    """Add html content together"""

    old_html += raw_html
    return old_html
