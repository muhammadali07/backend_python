def ResponseOutCustom(message, status, data):
    out_rsp = {
        "message_id" : message,
        "status" : status,
        "data" : data
    }
    return out_rsp
