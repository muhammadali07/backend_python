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

@app.route("/") 
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



if __name__ == "__main__":
    migrate_basemodel()
    app.run(debug=True)
