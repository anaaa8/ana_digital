import streamlit as st

# Set page configuration at the very beginning of the script
st.set_page_config(page_title="Pengelolaan Keuangan Pribadi")

# Kelas untuk Pengelolaan Keuangan
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
        return self.saldo

    def lihat_transaksi(self):
        return self.transaksi

# Inisialisasi kelas PengelolaanKeuangan
keuangan = PengelolaanKeuangan()

# Judul aplikasi
st.title("Aplikasi Pengelolaan Keuangan Pribadi")

# Menu navigasi
menu = ["Tambah Pemasukan", "Tambah Pengeluaran", "Lihat Saldo", "Lihat Transaksi"]
pilihan = st.sidebar.selectbox("Pilih Menu", menu)

# Tambah Pemasukan
if pilihan == "Tambah Pemasukan":
    st.subheader("Tambah Pemasukan")
    jumlah = st.number_input("Masukkan jumlah pemasukan: Rp", min_value=0.0)
    keterangan = st.text_input("Masukkan keterangan")
    if st.button("Tambah"):
        keuangan.tambah_pemasukan(jumlah, keterangan)
        st.success("Pemasukan berhasil ditambahkan!")

# Tambah Pengeluaran
elif pilihan == "Tambah Pengeluaran":
    st.subheader("Tambah Pengeluaran")
    jumlah = st.number_input("Masukkan jumlah pengeluaran: Rp", min_value=0.0)
    keterangan = st.text_input("Masukkan keterangan")
    if st.button("Tambah"):
        keuangan.tambah_pengeluaran(jumlah, keterangan)
        st.success("Pengeluaran berhasil ditambahkan!")

# Lihat Saldo
elif pilihan == "Lihat Saldo":
    st.subheader("Lihat Saldo")
    saldo = keuangan.lihat_saldo()
    st.write(f"Saldo saat ini: Rp {saldo:.2f}")

# Lihat Transaksi
elif pilihan == "Lihat Transaksi":
    st.subheader("Lihat Transaksi")
    transaksi = keuangan.lihat_transaksi()
    if transaksi:
        for jenis, jumlah, keterangan in transaksi:
            st.write(f"{jenis}: Rp {jumlah:.2f} - {keterangan}")
    else:
        st.write("Belum ada transaksi")

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.set_page_config(page_title="Pengelolaan Keuangan Pribadi")
