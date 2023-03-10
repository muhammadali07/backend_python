import csv
import io
import sys
import os
from flask import Flask, request, jsonify, send_file, Response, make_response
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
         return jsonify({'result': 'Payload request not provided'})
    
    return {
        'result' : {
            'nama': data['nama'],
            'usia': data['usia'],
            'asal' : data['asal']
        } 
    }

@app.route('/biografi/', methods=['POST'])
def biografi():
    data = request.get_json()
    return jsonify(data)

@app.route('/export_file', methods=['POST'])
def export_file():
    data = request.get_json()
    print(data)
    try:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        print(parent_dir)
        save_dir = os.path.abspath(f'{parent_dir}/download')
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # nama file
        file_name = 'data.csv'

        # buat file csv 
        with open(os.path.join(save_dir, file_name), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Nama', 'Usia', 'Asal'])
            for item in data:
                print(item)
                writer.writerow([item['nama'], item['usia'], item['asal']])
        
        # Kirimkan file ke client
        response = make_response(send_file(os.path.join(save_dir, file_name), mimetype='text/csv'))
        response.headers.set('Content-Disposition', 'attachment', filename=file_name)
        return response
        # return send_file(os.path.join(save_dir, file_name),
        #                 mimetype='text/csv',
        #                 as_attachment=True,
        #                 attachment_filename=file_name)
    except Exception as e :
        return str(e)


 

if __name__ == "__main__":
     app.run(debug=True)