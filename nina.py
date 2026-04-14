keranjang = []
print("Keranjang belanja siap!")

def tambah(item): keranjang.append(item)
tambah("Apel"); print(keranjang)

keranjang = ["Apel"]
def tambah(item): keranjang.append(item)
def lihat(): print(f"Isi: {keranjang}")
lihat()

keranjang = ["Apel"]
def tambah(item): keranjang.append(item)
def hapus(): keranjang.pop() if keranjang else None
hapus(); print(f"Setelah hapus: {keranjang}")keranjang = []
while True:
    item = input("Masukkan barang (ketik 'stop' untuk keluar): ")
    if item == 'stop': break
    keranjang.append(item)
    print(f"Isi keranjang: {keranjang}")

