from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gene-lookup/<gene_name>")
def gene_lookup(gene_name):
    # your code goes here!

    return "<p>Replace me!</p>"
