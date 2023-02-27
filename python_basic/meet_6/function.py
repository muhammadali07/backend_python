'''
def nama_function(parameter):
    kode/pernyataan fungsi
'''

def hello_word():
    print("hello world")

# fungsi tanpa return
def helloworld():
    print("Hello World")
    name = input("masukkan nama anda: ")
    print(f'Hai {name}, Selamat belajar python !!!')

helloworld()


# fungsi dengan return
a = 10
def pangkat(nilai):
    hasil = nilai **2
    return hasil

nilai_2 = pangkat(a)*2
print(nilai_2)

hello_word()