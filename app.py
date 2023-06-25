from flask import Flask, render_template, request, jsonify, make_response
from data.online import online
from data.fandomgt import gtfandom
import os, json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def home():
    return "Halaman Utama!"

@app.route('/api', methods=['GET','POST'])
def api():
    return render_template('api_s.html')

@app.route('/api/onlinegt', methods=['GET', 'POST'])
def onlinegt():
    on = online()
    print(on)
    return {"online":on}

@app.route('/api/gtwiki', methods=['GET', 'POST'])
def gtwiki():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return gtfandom(keyword)
    else:
        return {'error':"querykeyword"}


app.run(host='0.0.0.0', port=int(os.environ.get('port','5000')),debug=True)