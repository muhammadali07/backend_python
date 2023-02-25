for i in range(1,5):
    if i is 2:
        print("nilai",i,"ditemukan")
        continue
        print("nilai setelah continue") # nilai tidak akan dicetak jika proses terpenuhi
    print("nilai saat ini adalah",i)

# hasil :
# nilai saat ini adalah 1
# nilai 2 ditemukan
# nilai saat ini adalah 3
# nilai saat ini adalah 4