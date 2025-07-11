# Import required libraries
from flask import Flask, render_template, request, session, redirect, url_for
from textblob import TextBlob

# Create a Flask application instance
app = Flask(__name__)

# Secret key is required to use session variables securely
app.secret_key = 'your_secret_key'  # Replace with a strong random key in production

# Define the main route (home page) with GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def analyze():
    # If 'history' does not exist in session, initialize it as an empty list
    if 'history' not in session:
        session['history'] = []

    # Initialize variables
    sentiment = polarity = subjectivity = word_count = None

    # Check if the form is submitted (POST request)
    if request.method == 'POST':
        # Get text input from the form
        text = request.form['text']

        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 3)         # Polarity (-1 to 1)
        subjectivity = round(blob.sentiment.subjectivity, 3) # Subjectivity (0 to 1)
        word_count = len(text.split())                       # Count number of words

        # Determine overall sentiment based on polarity value
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Append the result to the session history
        session['history'].append({
            'text': text,
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'word_count': word_count
        })

        # Mark session as modified so changes are saved
        session.modified = True

    # Render the HTML template and pass variables to it
    return render_template('index.html',
                           sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity,
                           word_count=word_count,
                           history=session.get('history', []))  # Pass history to template

# Define route to clear the history
@app.route('/clear')
def clear_history():
    session.pop('history', None)  # Remove 'history' from session
    return redirect(url_for('analyze'))  # Redirect to the main page

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
