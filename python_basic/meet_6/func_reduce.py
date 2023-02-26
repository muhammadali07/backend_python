from functools import reduce
data = [3,6,2,8,6,9,3]

def cek_maks(a,b):
  if a > b:
    return a
  else:
    return b

hasil  = reduce(cek_maks,data)
print(hasil)