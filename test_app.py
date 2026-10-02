from app import tambah

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0
    print("Semua tes berhasil!")

if __name__ == "__main__":
    test_tambah()