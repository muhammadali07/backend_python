# lulus = input("Apakah kamu lulus? [ya/tidak]: ")

# if lulus == "tidak":
#    print("Kamu harus ikut ujian")

# if lulus == "tidak":
# print("Kamu harus ikut remidi")

#program untuk mengecek bonus dan diskon
# file: bonus.py

total_belanja = input("Total belanja: Rp ")

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
bayar = int(total_belanja)

# jika dia belanja di atas 100rb maka berikan bonus dan diskon
if int(total_belanja) > 100000:
    print("Kamu mendapatkan bonus minuman dingin")
    print("dan diskon 5%")

    # hitung diskonnya
    diskon = int(total_belanja) * 5/100 #5%
    bayar = int(total_belanja) - diskon


# cetak struk
print("Total yang harus dibayar: Rp %s" % bayar)
print(f'Total potongan Diskon : {diskon}')
print("Terima kasih sudah berbelanja")
print("Datang lagi yaa...")
