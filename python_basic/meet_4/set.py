# cara pertama
set_01 = {"anwar", "dwija", "kinanti", "rida", "dwija"}
print(set_01)

# cara kedua
set_02 = set()
set_03 = set([2,1,4,3])

print(type(set_02))
print(type(set_03), set_03)

# menghapus anggota set
set_01 = {4,5,6,2}

#menggunakan discard()
set_01.discard(4)
print(set_01)

#menggunakan remove()
set_01.remove(2)
print(set_01)

# mengubah & menambah anggota set

set_04 = {2,3,4,5,6}

set_04.add(1)
print(set_04)

# operasi set
set_A = {1,2,3,4}
set_B = {3,4,5,6}

# union
print(set_A|set_B)
print(set_A.union(set_B))

# intersection
print(set_A & set_B)
print(set_A.intersection(set_B))

# difference
print(set_A - set_B)
print(set_A.difference(set_B))

#symmetric difference
print(set_A ^ set_B)
print(set_A.symmetric_difference(set_B))