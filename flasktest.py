# VIDEO TO REVIEW FLASK NOT USED FOR PortSploit

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def test(): 
    return "This is working"

app.run(host="0.0.0.0", port=80)