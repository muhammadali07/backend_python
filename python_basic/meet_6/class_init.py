class mobil:
    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna

mobil1 = mobil('Sedan', 'Merah')
mobil2 = mobil('SUV', 'Hitam')

print(mobil1.__dict__)
print(mobil2.__dict__)