from flask import Flask, render_template
# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    """Show portfolio of stocks"""

    return render_template("index.html")

@app.route("/tracker")
def tracker():
    """Show portfolio of stocks"""

    return render_template("tracker.html")

@app.route("/newsletter")
def newsletter():
    """Show portfolio of stocks"""

    return render_template("newsletter.html")

@app.route("/resources")
def resources():
    """Show portfolio of stocks"""

    return render_template("resources.html")

