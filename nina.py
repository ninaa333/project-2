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
hapus(); print(f"Setelah hapus: {keranjang}")