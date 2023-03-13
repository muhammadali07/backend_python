import csv
import io
import sys
import os
from flask import Flask, request, jsonify, send_file, Response, make_response
from flask_cors import CORS, cross_origin

from utils import migrate_basemodel
# import crud modul
from crud import trainer_crud

app = Flask(__name__)
CORS(app=app)

@app.route("/") 
@cross_origin
def main():
     return "Welcome Ihsan API!"

@app.route('/create_data_trainer', methods=["POST"])
def create_data_trainer():
     dRquest = request.get_json()
     result = trainer_crud.create_data(dRquest)
     return jsonify(result)


@app.route('/get_list_data', methods=['GET'])
def get_list_data():
     dRequest = request.get_json()
     keyword = dRequest['data']['keywords']
     limit = dRequest['data']['limit']
     page = dRequest['data']['page']
     result = trainer_crud.get_list_data(
          keyword=keyword,
          limit=limit,
          page=page
     )
     return jsonify(result)

@app.route('/get_list_data_id/<id>', methods=['GET'])
def get_list_data_id(id):
     result = trainer_crud.get_list_data_id(id)
     return jsonify(result)

@app.route('/update-data-by-id/<id>', methods=['PUT'])
def update_data_by_id(id):
     data = request.get_json()
     name_trainer = data['name_trainer']
     result = trainer_crud.update_data_by_id(id, name_trainer=name_trainer)
     return jsonify(result)


@app.route('/delete-data-by-id/<id>', methods=['DELETE'])
def delete_data_by_id(id):
     result = trainer_crud.delete_data_by_id(id)
     return jsonify(result)

@app.route('/update_data_with_patch_id/<id>', methods=['PATCH'])
def update_with_path(id):
     data = request.get_json()
     trainer_kelas = data['trainer_kelas']
     result = trainer_crud.update_with_path(
          id=id,
          trainer_kelas=trainer_kelas
     )
     return jsonify(result)


if __name__ == "__main__":
    migrate_basemodel()
    app.run(debug=True)
