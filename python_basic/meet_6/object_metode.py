class mobil:
    def __init__(self, jenis, warna, tangki, efisiensi):
        self.jenis = jenis
        self.warna = warna
        self.tangki = tangki
        self.efisiensi = efisiensi
    def data_mobil(self):
        print("mobil saya berjenis",self.jenis,"dan memiliki warna",self.warna,"serta memiliki ukuran tangki",self.tangki,"L")

    def sisa_bensin(self,jarak):
        sisa = self.tangki - ((jarak/10)*self.efisiensi)
        return print("sisa bensin adalah",sisa)

mobil1 = mobil('Sedan', 'Merah', 40, 4)

mobil1.sisa_bensin(20)