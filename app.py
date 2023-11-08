from flask import Flask, render_template, request, jsonify, make_response, send_file
from data.online import online
from data.sertitolol import serti
from data.gtfandom import fandomgt
import os, json
import qrcode

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
        return {'error':"Keyword Input Please"}

@app.route('/api/sertitolol', methods=['GET', 'POST'])
def sertitolols():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return serti(keyword)
    else:
        return {'error':"Keyword Input Please"}

@app.route('/api/qrcode', methods=['GET','POST'])
def qrcode_gen():
    if request.args.get('keyword'):
        try:
            input_data = request.args.get('keyword')
            qr = qrcode.QRCode(
            version=2,
            box_size=15,
            border=2)
            qr.add_data(input_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save('data/qrcode.png')
            return send_file('data/qrcode.png')
        except Exception as e:
            print(e)
            return{
                'result': 'Gagal membuat qr!'
            }
    else:
        return{
            'result': 'Masukkan parameter text!'
        }


app.run(host='0.0.0.0', port=int(os.environ.get('port','5000')),debug=True)
