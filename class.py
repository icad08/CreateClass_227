class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    print("Selamat datang di program Persegi Panjang!")
    
    # Input panjang dan lebar
    panjang = float(input("Masukkan panjang (cm): "))
    lebar = float(input("Masukkan lebar (cm): "))
    
    # Membuat objek PersegiPanjang
    pp = PersegiPanjang(panjang, lebar)
    
    print(pp)  # Menampilkan informasi tentang persegi panjang
    
    while True:
        print("\nPilih opsi:")
        print("1. Hitung Keliling")
        print("2. Hitung Luas")
        print("3. Keluar")
        
        opsi = input("Masukkan pilihan (1/2/3): ")
        
        if opsi == '1':
            keliling = pp.hitung_keliling()
            print(f"Keliling: {keliling} cm")
        elif opsi == '2':
            luas = pp.hitung_luas()
            print(f"Luas: {luas} cm²")
        elif opsi == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()