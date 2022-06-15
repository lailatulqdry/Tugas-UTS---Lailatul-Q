class Costumer:
    def __init__(self, name ):
        self.name = name
    
    def cetakNama(self):
        print('Selamat Datang Pelanggan Setia  ' + self.name )

nc = Costumer('Abadi Jaya')
nc.cetakNama()

a = input('Masukkan Nama Anda : ')
b = int(input('Total belanja Rp. '))
if b > 30000:
    print('Selamat Anda mendapatkan diskon 5%')

    diskon = b * 5/100
    bayar = b - diskon

    print('Total belanja Rp.', b)
    print('Potongan harga Rp. ', diskon)
    print('Total Pembayaran Rp. ', bayar)
else:
    print('Maaf, total belanjaan anda kurang dari 30.000')

print('Terimakasih Sudah Berbelanja Di Toko Kami')