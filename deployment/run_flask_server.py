from utils import generate_reviews, predict_sentiment
import tensorflow
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from flask import Flask, render_template, request
from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField

# Create app
app = Flask(__name__)


class ReusableForm(Form):
    """User entry form for entering specifics for generation"""
    # Starting seed
    seed = TextField("Enter a seed string or 'random':", validators=[
                     validators.InputRequired()])
    # Diversity of predictions
    diversity = DecimalField('Enter diversity:', default=0.8,
                             validators=[validators.InputRequired(),
                                         validators.NumberRange(min=0.5, max=5.0,
                                                                message='Diversity must be between 0.5 and 5.')])
    # Number of words
    words = IntegerField('Enter number of words to generate:',
                         default=50, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=10, max=100, message='Number of words must be between 10 and 100')])
    # Submit button
    submit = SubmitField("Enter")


def load_data():
    """Load in the pre-trained model, prefit text tokenizer and test data"""
    global model
    model = load_model("../models/model_trained_embedding.h5")
    global tokenizer
    with open("../models/tokenizer.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    global test_data
    with open("../models/test_data.pickle", "rb") as handle:
        test_data = pickle.load(handle)
    global test_texts
    with open("../models/test_texts.pickle", "rb") as handle:
        test_texts = pickle.load(handle)
    global test_labels
    with open("../models/test_labels.pickle", "rb") as handle:
        test_labels = pickle.load(handle)


# old page
@app.route("/old", methods=['GET', 'POST'])
def old():
    """Home page of app with form"""
    # Create form
    form = ReusableForm(request.form)

    # On form entry and all conditions met
    if request.method == 'POST' and form.validate():
        # Extract information
        seed = request.form['seed']
        diversity = float(request.form['diversity'])
        words = int(request.form['words'])
        # Generate a random sequence
        if seed == 'random':
            return render_template('random.html', input=generate_random_start())
        # Generate starting from a seed sequence
        else:
            return render_template('seeded.html', input=generate_from_seed())
    # Send template information to index.html
    return render_template('index.html', form=form)

#home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    form = ReusableForm(request.form)
    if request.method == 'POST':
        if 'predict_button' in request.form:
            return render_template('prediction.html', form=form, review= request.form['user_text'],
                                   input= predict_sentiment(model, tokenizer, request.form['user_text']))

    return render_template('home.html', form=form, table_data= generate_reviews(model, test_data, test_labels, test_texts))

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    load_data()
    # Run app
    app.run(host="localhost", port=8080)
