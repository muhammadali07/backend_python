# from datetime import datetime as dtm
# masuk_str = '05-08-2005 07:35:12'
# masuk_date = dtm.strptime(masuk_str,'%d-%m-%Y %H:%M:%S')
# print(masuk_date, type(masuk_date))


from datetime import datetime as dtm

tgl_text = '02-03-2023'
print(tgl_text, type(tgl_text))  # tipe data str

# konversi string ke date dengan format tertentu
tgl_date = dtm.strptime(tgl_text, '%d-%m-%Y')
print(tgl_date, type(tgl_date))  # tipe data datetime.datetime

# contoh 2
masuk_str = '01-03-2023 13:54:20'
masuk_date = dtm.strptime(masuk_str, '%d-%m-%Y %H:%M:%S')
print(masuk_date, type(masuk_date))