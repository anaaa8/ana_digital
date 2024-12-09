import streamlit as st
class PengelolaanKeuangan:
    def __init__(self):
        self.saldo = 0.0
        self.transaksi = []

    def tambah_pemasukan(self, jumlah, keterangan):
        self.saldo += jumlah
        self.transaksi.append(('Pemasukan', jumlah, keterangan))

    def tambah_pengeluaran(self, jumlah, keterangan):
        self.saldo -= jumlah
        self.transaksi.append(('Pengeluaran', jumlah, keterangan))

    def lihat_saldo(self):
        print(f"Saldo saat ini: Rp {self.saldo:.2f}")

    def lihat_transaksi(self):
        print("Riwayat Transaksi:")
        for jenis, jumlah, keterangan in self.transaksi:
            print(f"{jenis}: Rp {jumlah:.2f} - {keterangan}")

def menu():
    keuangan = PengelolaanKeuangan()
    while True:
        print("\n--- Aplikasi Pengelolaan Keuangan Pribadi ---")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Lihat Saldo")
        print("4. Lihat Transaksi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            jumlah = float(input("Masukkan jumlah pemasukan: Rp "))
            keterangan = input("Masukkan keterangan: ")
            keuangan.tambah_pemasukan(jumlah, keterangan)
            print("Pemasukan berhasil ditambahkan!")
        elif pilihan == '2':
            jumlah = float(input("Masukkan jumlah pengeluaran: Rp "))
            keterangan = input("Masukkan keterangan: ")
            keuangan.tambah_pengeluaran(jumlah, keterangan)
            print("Pengeluaran berhasil ditambahkan!")
        elif pilihan == '3':
            keuangan.lihat_saldo()
        elif pilihan == '4':
            keuangan.lihat_transaksi()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()
