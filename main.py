from flask import Flask, url_for, render_template
from configuration import configure_all
app = Flask(__name__)

configure_all(app)

app.run(debug=True, port=80)
