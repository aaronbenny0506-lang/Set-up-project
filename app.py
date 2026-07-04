"""
app.py
A basic Flask web application.

Run locally with:
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    """Render the homepage."""
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/about")
def about():
    """Render a simple about page."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
