response = {"status": "Success", "message":"Data tidak di temukan", "data":[]}

datax = {
    'name': 'Muh Ali Bakhtiar',
    'tgl' : '17 Agustus 1945',
    'pekerjaan': 'Trainer BE Python'
}

response['data'].append(datax)

print(response)