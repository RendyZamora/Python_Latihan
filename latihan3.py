# import os
# os.system('cls')
mahasiswa = {
    'nama': 'Andi',
    'umur': 21,
    'jurusan': 'Informatika'
}

data = dict.fromkeys(mahasiswa, 'kosong')
data.update(mahasiswa)
mahasiswa1 = mahasiswa.keys()
data['nama'] = input("Masukkan nama mahasiswa: ")
print(f"{10*'='} MAHASISWA {10*'='}")
print(data)
print(mahasiswa1)