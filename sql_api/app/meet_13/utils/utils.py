def ResponseOutCustom(message_id, status, data):
    out_resp = {
        "message": message_id,
        "status": status,
        "data": data
        
    }
    return out_resp

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d