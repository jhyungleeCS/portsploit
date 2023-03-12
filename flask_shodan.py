from flask import Flask, render_template, request
from shodan_funcAPI import search_org

app = Flask(__name__)

# Working route function 
@app.route('/')
def index():
    #return render_template('index.html')
    return "This is Working"

# Running on Local Host 
app.run(host="0.0.0.0", port=80)

#@app.route('/search', methods=['POST'])
#def search():
 #   org = request.form['org']
  #  results = search_org(org)
   # return render_template('search.html', org=org, results=results)

#if __name__ == '__main__':
    #app.run()


