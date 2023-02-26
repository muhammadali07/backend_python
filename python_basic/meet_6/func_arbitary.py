#contoh fungsi args
def fungsi_05 (*nama):
  for item in nama:
    print(item)


fungsi_05('rudi','santi','mirna')


#contoh fungsi kwargs
def fungsi_06 (**nama):
  for key, value in nama.items():
    print(key, value)

fungsi_06(nama = 'rudi', umur = 18)