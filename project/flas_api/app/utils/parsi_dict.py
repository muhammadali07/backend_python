import json
from flask import jsonify
def as_dict(list_data):
    dtln = []
    for data in list_data:
        _dict = data.__dict__.copy()
        _dict.pop('_sa_instance_state', None)
        rsp = jsonify(_dict)
        reps = json.loads(rsp.data)
        dtln.append(reps)
    
    return dtln