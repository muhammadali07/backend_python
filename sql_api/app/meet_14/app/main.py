from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

 

@app.route("/") 
def main():
     return "Welcome!"

@app.route('/nama/', methods=["GET"])
def nama1():
     return "Halo nama saya adalah Ihsan Solusi"

@app.route('/nama/<name>', methods=["GET"])
@cross_origin()
def nama(name):
    usia = request.args.get('age')
    asal = request.args.get('from')
    return {
        'result' : {
            'nama': name,
            'usia': usia,
            'asal' : asal
        }
    }

@app.route('/biodata/', methods=['POST'])
def bio():
    data = request.get_json()
    if data is None:
         return jsonify({'result': 'Payload request not provided'}), 400
    
    return {
        'result' : {
            'nama': data['nama'],
            'usia': data['usia'],
            'asal' : data['asal']
        } 
    }, 200

@app.route('/biografi/', methods=['POST'])
def biografi():
    data = request.get_json()
    return jsonify(data)
 

if __name__ == "__main__":
     app.run(debug=True)