#! usr/bin python3

from flask import Flask, render_template, request
from shodan_funcAPI import search_org
import shodan 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    org = 'Drexel University'
    port = request.form['port']
    results = search_org(org, port)
    return render_template('result.html', results=results)


# Running on Local Host 
app.run(host="0.0.0.0", port=80)



