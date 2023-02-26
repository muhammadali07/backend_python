data = [1,2,3,4]

def cek_genap(nilai):
   if nilai % 2 == 0:
      return True
   return False
hasil = list(filter(cek_genap,data)) 
print(hasil)