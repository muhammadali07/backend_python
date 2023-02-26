class mobil:

    def __init__(self, jenis, warna, tangki):
        self.jenis = jenis
        self.warna = warna
        self.tangki = tangki
    
    def data_mobil(self):
        print("mobil saya berjenis",self.jenis,"dan memiliki warna",self.warna,"serta memiliki ukuran tangki",self.tangki,"L")

mobil1 = mobil('Sedan', 'Merah', 40)

mobil1.data_mobil()