a = 10
b = 0
try:
  hasil = a/b
  print(hasil)
except TypeError:
  print('Kesalahan pada unit perhitungan')
except ZeroDivisionError:
  print('Membagi dengan nilai 0')
