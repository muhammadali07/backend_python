import json
file = open('file/file_03.json')
data = json.load(file)


# apa bedanya json.load dan json.loads ?
'''
json.load() :  Mengambil objek file dan mengembalikan objek JSON. 
               Ini digunakan untuk membaca data yang dikodekan JSON dari file dan mengubahnya menjadi Python dictionary
               dan mendeserialisasi file itu sendiri yaitu menerima objek file.

json.loads() : metode dapat digunakan untuk mengurai string JSON yang valid dan mengubahnya menjadi Python dictionary. 
               Ini terutama digunakan untuk deserialisasi string asli, byte, atau array byte yang terdiri dari data JSON ke dalam Python Dictionary.
'''
print(data)