from flask import Flask, render_template, request
from shodanplayground import search_org

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    org = request.form['org']
    results = search_org(org)
    return render_template('search.html', org=org, results=results)

if __name__ == '__main__':
    app.run()

print("Hello World")
