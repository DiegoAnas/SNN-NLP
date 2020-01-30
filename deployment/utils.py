import numpy as np
from random import randrange
import json
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def generate_reviews(model, test_data, test_y, test_texts):
    reviews = {}
    for i in range(1,10):
        review = (randrange(len(test_texts)))
        prediction_score = model.predict([test_data[review:review+1]])[0][0]
        reviews[str(i)] = ({'Review': test_texts[review],
                            'Prediction': prediction_score,
                            'Truth': test_y[review],
                            'Correct': (prediction_score > 0.5 and test_y[review] == 1) or
                                           (prediction_score < 0.5 and test_y[review] == 0) })
    return reviews


def predict_sentiment(model, tokenizer, text):
    sequenced_text = tokenizer.texts_to_sequences([text,])
    seq_evaluate = pad_sequences(sequenced_text, maxlen=400)
    prediction_score = model.predict([seq_evaluate,])[0][0]
    return prediction_score


def generate_random_start():
    """Generate `new_words` words of output from a trained model and format into HTML."""

    # HTML formatting
    seed_html = ''
    seed_html = addContent(seed_html, header(
        'Seed Sequence', color='darkblue'))
    seed_html = addContent(seed_html, box("Test seed box"))

    gen_html = ''
    gen_html = addContent(gen_html, header('RNN Generated', color='darkred'))
    gen_html = addContent(gen_html, box("Test gen box"))

    a_html = ''
    a_html = addContent(a_html, header('Actual', color='darkgreen'))
    a_html = addContent(a_html, box("Test a box"))

    return f'<div>{seed_html}</div><div>{gen_html}</div><div>{a_html}</div>'


def generate_from_seed():
    """Generate output from a sequence"""
    html = ''
    html = addContent(html, header(
        'Input Seed ', color='black', gen_text='Network Output'))
    html = addContent(html, box("seed text", "gen text"))
    return f'<div>{html}</div>'


def header(text, color='black', gen_text=None):
    """Create an HTML header"""

    if gen_text:
        raw_html = f'<h1 style="margin-top:16px;color: {color};font-size:54px"><center>' + str(
            text) + '<span style="color: red">' + str(gen_text) + '</center></h1>'
    else:
        raw_html = f'<h1 style="margin-top:12px;color: {color};font-size:54px"><center>' + str(
            text) + '</center></h1>'
    return raw_html


def box(text, gen_text=None):
    """Create an HTML box of text"""

    if gen_text:
        raw_html = '<div style="padding:8px;font-size:28px;margin-top:28px;margin-bottom:14px;">' + str(
            text) + '<span style="color: red">' + str(gen_text) + '</div>'

    else:
        raw_html = '<div style="border-bottom:1px inset black;border-top:1px inset black;padding:8px;font-size: 28px;">' + str(
            text) + '</div>'
    return raw_html


def addContent(old_html, raw_html):
    """Add html content together"""

    old_html += raw_html
    return old_html


def format_sequence(s):
    """Add spaces around punctuation and remove references to images/citations."""

    # Add spaces around punctuation
    s = re.sub(r'(?<=[^\s0-9])(?=[.,;?])', r' ', s)

    # Remove references to figures
    s = re.sub(r'\((\d+)\)', r'', s)

    # Remove double spaces
    s = re.sub(r'\s\s', ' ', s)
    return s


def remove_spaces(s):
    """Remove spaces around punctuation"""

    s = re.sub(r'\s+([.,;?])', r'\1', s)

    return s
