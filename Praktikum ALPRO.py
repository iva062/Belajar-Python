'''MODUL 1'''
print('---MODUL 1---')
print()

'''Latihan'''
print('Latihan:')

nama = "Iva"
umur = 17
tinggi = 155
mahasiswa = True

#mencetak variabel ke layar
print('Nama: ', nama)
print('Umur: ', umur)
print('Tinggi: ', tinggi)
print('Mahasiswa: ', mahasiswa)

#perubaan nilai pada variabel
umur = 19
print("Umur setelah ulang tahun: ", umur)

#tipe data
#mengecek tipe data
print("Tipe data dari variabel 'nama':", type(nama))
print("Tipe data dari variabel 'umur':", type(umur))
print("Tipe data dari variabel 'tinggi':", type(tinggi))
print("Tipe data dari variabel 'mahasiswa':", type(mahasiswa))

#konversi tipe data
angka = 22
print("Tipe data sebelum konversi: ", type(angka))

#konversi string ke integer 
angka = int(angka)
print("Tipe data sebelum konversi: ", type(angka))

a=5
b=3
result=a+b
print("result", result)

message = "umur saya " +str (umur) + "tahun"
print("umur saya:", message)
print()

'''Tugas Individu Modul 1'''
print('Tugas Individu Modul 1')

#TUGAS 1
#menginput nilai berupa string
satu = input("Masukkan angka: ")
print(satu)
print(type(satu))

#mengonversi string ke integer
satu = int(input("Masukkan angka: "))
print("Tipe data setelah konversi: ", type(satu))

#mengonversi string ke float
satu = float(input("Masukkan angka: "))
print("Tipe data setelah konversi: ", type(satu))
print()

#TUGAS 2
#menampilkan output 'False'
print("False")

#menampilkan tipe data boolean berupa 'False'
pembohong = False
print(type(pembohong))

#menampilkan teks didalam string
dua = "Ini adalah tulisan berupa string"
print(dua)

#melakukan penjumlahan aritmatika berupa penjumlahan
a = 49
b = 51
print(a+b)

#melakukan penjumlahan aritmatika berupa pembagian
c = 1
d = 1000
hasil = c/d
print(hasil)

#menampilkan teks dalam tipe data string
tiga = "bilangan desimal dari 0x01 adalah 1"
print(tiga)

##melakukan penjumlahan aritmatika berupa  pembagian
e = 100
f = 10
hasil = e/f
print(hasil)

#menampilkan tipe data complex
bilangan = a+2j
print(type(bilangan))

#menampilkan output (2+6j)
print("(2+6j)")

#menampilkan tipe data complex
lima = a+7j
print(type(lima))

#menampilkan data dalam tipe data list
enam = [96, 97, 98, 99, 100]
print(enam)

#menampilkan data dalam tipe data list
tujuh = ['seratus', 'dua ratus', 'tiga ratus']
print(tujuh)

#menampilkan data dalam tipe data dictionary
cortis = {'nama': 'Riz', 'umur': 19}
print(cortis)
print()

'''MODUL 2
Value, Assignment, Input/Output, dan Expression'''
print('MODUL 2')

#1. Value, Value merupakan data yang disimpan di dalam variabel.
#   Value dibagi menjadi beberapa tipe yang berbeda: integer (bil. bulat), float(desimal), string, boolean.

print(5)
print('z')
print('True')

x=5
print(x,'tipenya adalah: ', type(x))
y=0.2
print(y,'tipenya adalah: ', type(y))
z='Hai'
print(z,'tipenya adalah: ', type(z))

#2. Assigment, Assigment adalah proses memberikan atau mengubah nilai variabel setelah variabel tsb di inisialisasi.
#   assignment dalam Python adalah proses menempatkan nilai ke dalam sebuah variabel. Dalam Python, assignment dilakukan dengan tanda =

x=10
y=5+7

#3. Input, data/masukan yang dibutuhkan supaya program bisa berjalan. 
#Proses, langkah langkah yang dilakukan oleh program untuk memecahkan masalah.
#Output, hasil yang didapatkan setelah menjalankan langkah-langkah tersebu

inp = input()
print(inp)

name= input('Siapa namamu? \n') #\n mewakili baris baru/ganti baris hingga input pengguna muncul dibawah prompt.
print(name)

#4. Expression, representasi dari nilai dan dapat terdiri dari gabungan antara values, variable dan operator.
#ekspresi aritmatika
x=10
y=3

print(x+y)
print(x-y)
print(x*y)

#ekspresi perbandingan
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)

#ekspresi logika
a= True
b= False
print(a and b)
print(a or b)
print(not a)
print()

#LATIHAN
print('Latihan:')

#1. Membuat dan memberikan nilai variabel
Nama = input("Nama Anda : ")
Alamat = input("Alamat Tinggal Anda : " )
Umur = input("Umur Anda : ")
TL = input("Tempat Lahir Anda : ")
Tgl = input("Tanggal Lahir Anda : ")
IPK = input("IPK Anda : ")
print("DATA AKADEMIK")
print("Nama Anda : ", Nama)
print("Alamat Tinggal Anda : ",Alamat)
print("Umur Anda : ", Umur)
print("Tempat Lahir Anda : ", TL)
print("Tanggal Lahir Anda : ", Tgl)
print("IPK Anda :", IPK)

x1 = eval(input("X1 = "))
x2 = eval(input("X2 = "))
x3 = eval(input("X3 = "))
x4 = eval(input("X4 = "))
jumlah = x1+x2+x3+x4
kali = x1*x2*x3*x4
print(' ')
print('Hasil Penjumlah semua bilangan = ', jumlah)
print('Hasil Perkalian semua bilangan = ', kali)
jumlah = jumlah + 0.5
print('Jika ditambah 0.5 hasilnya = ',jumlah)
kali = kali * 0.5
print('Jika dikali 0.5 hasilnya = ',kali)

#2. Melakukan Assigment
total_hrg_brg= 0.0
kd_brg=input("Kode barang = ")
nama_brg=input("Nama barang = ")
harga_satuan=eval(input("Harga satuan barang =Rp. "))
jum_brg=eval(input("Jumlah barang yang dibeli = "))
harga_beli = harga_satuan * jum_brg
total_hrg_brg= harga_beli + total_hrg_brg
print("Total harga yang dibayar Rp",total_hrg_brg)
print()

#TUGAS INDIVIDU
print('Tugas individu:')
# 1
#menginput nama, umur, dan tahun masuk kuliah
nama = input('Masukkan nama anda: ')    
umur = int(input('Masukkan umur anda: '))
tahun_masuk_kuliah = int(input('Masukkan tahun anda masuk kuliah: '))
lulus = 4 #diasumsikan kelulusan yaitu 4 tahun
umur_saat_lulus = umur + lulus #menghitung umur saat lulus nanti

#menampilkan hasil output
print('-----Data mahasiswa-----')
print('Nama: ', nama)
print('Umur: ', umur)
print('Tahun masuk kuliah: ', tahun_masuk_kuliah)
print('Umur saat kelulusan: ', umur_saat_lulus)

print()

# 2
harga_barang = 50000                #barang dijual dengan harga Rp 50.000,00
jumlah_barang = int(input('Masukkan jumlah barang yang anda beli: '))
total_harga = jumlah_barang * harga_barang #menghitung total belanja dengan mengalikan jumlah barang dan harga barang
if total_harga >= 200000:           #jika total belanja lebih dari Rp200.000,- akan mendapat diskon 10%
    diskon = total_harga * 0.1
else:                               #jika total belanja kurang dari Rp200.000,- tidak mendapat diskon
    diskon = 0
harga_akhir = total_harga - diskon  #menghitung harga akhir setelah total belanja dikurangi diskon

#menampilkan hasil output
print('Harga barang: ', harga_barang)
print('Jumlah barang: ', jumlah_barang)
print('Jumlah diskon: ', diskon)
print('Harga akhir nyang harus dibayar: ', harga_akhir)

'''MODUL 3'''

# Bekerja dengan Pernyataan If
'''jika angka tersebut kurang dari nol,
pesan yang menyatakan hal ini akan dicetak kepada pengguna
Jika angkanya positif, maka tidak ada output'''

num = int(input('Masukkan sebuah angka: '))
if num < 0:
  print(num, 'adalah angka negatif')

'''pernyataan print('Bye') bukan bagian dari pernyataan if,
ini hanyalah pernyataan selanjutnya yang dieksekusi setelah
pernyataan if (dan pernyataan print terkait) selesai dieksekusi. '''

num = int(input('Masukkan angka lain: '))
if num > 0:
  print(num, 'adalah angka positif')
  print(num, 'kuadratnya adalah', num * num)
  print('Bye')

# Else dalam Pernyataan If
'''else dalam pernyataan if; elemen ini dapat dijalankan
jika bagian kondisional dari pernyataan if mengembalikan False'''

num = int(input('Masukkan angka lain lagi: '))
if num < 0:
  print('Angkanya negatif')
else:
  print('Angkanya tidak negatif')

# Penggunaan elif
'''Elemen elif dalam pernyataan if mengikuti bagian if dan muncul sebelum bagian else
(opsional)'''

savings = float(input("Masukkan jumlah tabungan Anda: "))
if savings == 0:
  print("Maaf, tidak ada tabungan")
elif savings < 500:
  print('Bagus sekali')
elif savings < 1000:
  print('Lumayan ya')
elif savings < 10000:
  print('Selamat Berjuang!')
else:
  print('Terima kasih')

# Menyusun Nested Pernyataan If
'''menyusun (nesting) satu pernyataan if di dalam pernyataan if lainnya.
Istilah nesting menunjukkan bahwa satu pernyataan if ditempatkan di dalam bagian
dari pernyataan if lainnya dan dapat digunakan untuk memperhalus perilaku kondisional dari program'''

snowing = True
temp = -1
if temp < 0:
  print('It is freezing')
  if snowing:
    print('Put on boots')
    print('Time for Hot Chocolate')
print('Bye')

# Ekspresi If
'''Ekspresi if adalah bentuk singkat dari pernyataan if yang mengembalikan nilai.
Ekspresi mengembalikan nilai, sedangkan pernyataan tidak.
Dengan menggunakan ekspresi if, kita dapat melakukan tes untuk menentukan
nilai yang akan diberikan ke status dan mengembalikannya sebagai hasil dari ekspresi if.'''

age = 19
status = None
status = ('remaja' if age > 12 and age < 20 else 'bukan remaja')
print(status)

# Latihan: menulis program kecil untuk menguji apakah sebuah bilangan bulat positif atau negatif.

# Minta pengguna untuk memasukkan angka
angka = input("Silakan masukkan sebuah angka: ")
# Ubah string menjadi bilangan bulat
angka = int(angka)
# Periksa apakah angka positif, negatif, atau nol
if angka > 0:
  print(f"{angka} adalah angka positif.")
elif angka < 0:
  print(f"{angka} adalah angka negatif.")
else:
  print("Angka tersebut adalah nol.")

# menguji apakah angka tersebut genap
angka = int(input("Silakan masukkan sebuah angka: "))

# menentukan apakah angka tersebut ganjil atau genap
if (angka % 2) == 0:
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")
print()

'''TUGAS INDIVIDU'''
#kasus 1

usia = int(input('Masukkan umur anda: '))
if usia < 3:                            
elif usia <= 12 and usia >= 3:          
    print('harga tiket Rp 150.000,00')
elif usia <= 65 and usia > 12:         
    print('harga tiket Rp 225.000,00')
else:                                   
    print('harga tiket Rp 180.000,00')


#kasus 2

nilai = int(input('Masukkan angka: '))
if nilai >= 1000 and nilai < 10000:                         
    print(nilai, 'adalah angka yang memiliki 4 digit')
else:
    print(nilai, 'adalah angka yang tidak memiliki 4 digit')

#kasus 3

angka = int(input('masukkan angka: '))
if (angka % 5) == 0:                                                                #kondisi jika angka adalah angka yg habis dibagi 5
    print(angka, 'adalah angka yang habis dibagi 5')
    if (angka % 3) == 0:                                                            #kondisi perulangan jika angka adalah angka yg habis dibagi 5 dan habis dibagi 3
        print(angka, 'adalah angka yang habis dibagi 5 dan habis dibagi 3')
    else:                                                                           #kondisi perulangan jika tidak memenuhi if dan elif
        print(angka, 'adalah angka yang habis dibagi 5 tapi tidak habis dibagi 3')
elif (angka % 3) == 0:                                                              #kondisi jika tidak memenuhi kondisi pertama
    print(angka, 'adalah angka yang habis dibagi 3')
    if (angka % 4) == 0:                                                            #kondisi perulangan jika angka adalah angka yg habis dibagi 3 dan habis dibagi 4
        print(angka, 'adalah angka yang habis dibagi 3 dan habis dibagi 4')
    else:                                                                           
        print(angka, 'adalah angka yang habis dibagi 3 dan tidak habis dibagi 4')
else:
    print(angka, 'adalah angka yang tidak habis dibagi 5 dan tidak habis dibagi 3')

#kasus 4

angka1 = int(input('masukkan angka: '))
angka2 = int(input('masukkan angka: '))
angka3 = int(input('masukkan angka: '))
if (angka1 % 2) == 0 and (angka2 % 2) == 0 and (angka3 % 2) == 0 :
    hasil = angka1 + angka2 + angka3
    print(angka1, angka2, angka3, 'adalah angka genap dan hasil penjumlahanm ketiganya adalah', hasil)
else:
    print(angka1, angka2, angka3, 'adalah angka tidak genap')

#kasus 5

jam = int(input('masukkan satuan jam: '))
hari = (jam/24)
if hari > 0:
    print(jam, 'jam jika dikonversi ke jumlah hari menjadi: ', hari, 'hari')
    print(jam, 'jam jika dikonversi ke jam sisa menjadi: ', hari, 'jam')
else:
    print(jam, 'jam jika dikonversi ke jumlah hari menjadi: ', hari, 'hari')
    print(jam, 'jam jika dikonversi ke jam sisa menjadi: ', hari, 'jam')

