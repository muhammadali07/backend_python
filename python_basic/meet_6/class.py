class mobil:
    pass

mobil_1 = mobil()
mobil_2 = mobil()

mobil_1.jenis = "Sedan"
mobil_1.warna = "Merah"

mobil_2.jenis = "SUV"
mobil_2.warna = "Hitam"

print(mobil_1)
print(mobil_1.jenis)
print(mobil_1.__dict__)