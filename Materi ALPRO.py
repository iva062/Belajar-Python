'''PERTEMUAN 2 (Flowchart, pseudecode, input, output, tipe data, dan operator)'''

#FLOWCHART
#PSEUDECODE
'''pseudecode berisi deskripsi dari algoritma pemrograman komputer yg menggunakan
struktur sederhana dari bbrp bahasa pemrograman agar mdh dimengerti dan dipahami
manusia.
-Penulisan pseudecode:
1. memiliki header: judul algoritma, komentar dan deklarasi
2. memiliki badan algoritma
3. memiliki bgian kahir algoritma'''
'''
contoh 1:
Program hitung_luas_lingkaran

deklarasi:
var number : integer

algoritma:
INPUT number
IF (number 2 = 0) THEN
        OUTPUT "genap"
ELSE 
        OUTPUT "ganjil"
'''
'''soal latihan: Buat pseudocode yang menerima input tahun dari pengguna,
lalu menentukan apakah tahun tersebut adalah tahun kabisat atau bukan!

(Tahun kabisat hanya berlaku pada tahun yang habis dibagi 4,
tetapi tidak berlaku untuk tahun yang habis dibagi 100,
kecuali jika juga habis dibagi 400)

jawaban:
Program penentuan tahun kabisat

deklarasi:
tahun : integer
hasil : string

algoritma:
INPUT tahun
IF (tahun MOD 400 == 0) THEN
    hasil = "Tahun kabisat"
ELIF (tahun MOD 4 == 0 AND tahun MOD 100 != 0) THEN
    hasil = "Tahun kabisat"
ELSE 
    hasil = "Bukan tahun kabisat"
END IF
OUTPUT hasil
'''

#INPUT
'''adalah proses memasukan data scr manual oleh user

contoh 1:'''
nama = input("Masukan nama anda: ")
nama = int(input("Masukkan umur anda: "))
'''contoh 2'''
umur = int(input("masukkan umur anda: ")) #nilai dlm variabel diubah ke integer agar tdk disimpan dlm string
umur = umur + 10
print("umur anda 10 tahun lagi adalah: ", umur)

#OUTPUT
'''adalah menampilkan suatu teks, angka, atau variabel dgn perintah print() dalam python

contoh 1:'''
print("halo, iva")
'''conton 2:'''
nama = "James,"
matkul = "Algoritma Pemrograman"
bahasa = "Python"
print(nama, "selamat Belajar", matkul, "dengan bahasa", bahasa, "ya!")

#latihan
nama = input("Masukkan nama anda: ")
tanggal_lahir = input("Masukkan tanggal lahir anda: ")
hobi = input("Masukkan hobi anda: ")
print("Selamat sudah mengisi formulir kami. Berikut data yang sudah anda input")
print("Nama:", nama)
print("Tanggal Lahir:", tanggal_lahir)
print("Hobi:", hobi)
print("Terima kasih, sukses selalu.")

#TIPE DATA
'''
1. string
2. integer, bilangan bulat
3. float, bilangan desimal
4. complex number, a=5j
5. boolean, true or false
6. list, tipe data didalamny tdk harus sama dan bersifat mutable, dpt diubah nilai/elemennya'''
cortis=[22,'james','martin','juhoon','sean','keonho', True, 22.1]
print(cortis)
cortis[0] = 'zhao yu fan'
print(cortis)
'''
7. tuple, tipe data didalamny tdk harus sama dan bersifat immutable, TIDAAK dpt diubah nilai/elemennya'''
cortis = (11, 'james','martin','juhoon','sean','keonho', True, 11.2)
print(cortis)
'''
8. set, tipe data didalamnya tdk berurutan dan TIDAK bs melakukan indexing,
output nya adalah data tdk akan diduplikat dan akan diurutkan'''
sean = {5,3,7,1,3,9,5}
print(sean)
'''
9. dictionary, kumpulan pasangan key value yg bersifat berurutan.'''
aku = {'nama':'iva','umur':19}
print(aku)
print(aku['nama']) #tdk bs indexing, harus mengetahui key nya utk akses nilai/elemen.
aku['nama'] = 'vava' #utk mengubah data
print(aku)
aku['hobi']='gambar' #utk menambahkan data, ckup masukan key dan value.
print(aku)
del aku['umur'] #untuk menghapus data
print(aku)

#OPERATOR
print()

'''PERTEMUAN 3
variabel, statement, expression, dan list'''

#KONSTANTA
'''berupa teks, angka, dan string yg nilainya tdk berubah
konstanta terdiri dari:
1. konstanta numerik, angka yg nilainya ttp dlm sbuah program'''
a=10     #integer
b=3,14   #float
c=-25    #integer negatif
d= 2.5e2 #notasi sains = 250.0
print(a,b,c,d)
'''
2. konstanta string, adlah teks yg nilainya ttp slama pemrograman berjalan.'''
nama1= "vava"
print("nama saya: ", nama1)

#VARIABEL
'''adalah wadah utk menyimpan nilai, komputer menyediakan ruang dimemori utk menyimpan nilainya.
1. nilai dlm variabel bs berubah-ubah slama pemrograman berjalan.
2. variabel bersifat dinamis, tdk perlu nyebut tipe data saat membuatnya.
3. nama variabel bersifat case sensitive, huruf besar kecil dibedakan.
4. tdk boleh mengandung kata kunci yg sdh ada di python (reseerve word) sprti if, while, dll
5. nama variabel diawali a-z dan 0-9 serta spasi dgn garis bawah (_)

Latihan'''
print()
print('latihan pertemuan kedua')

jari_jari =7
PI = 3.14
luas_lingkaran= PI*(jari_jari ** 2)
print(luas_lingkaran) #no.1 konstanta numerik

PESAN = 'Selamat belajar python'
print(PESAN) #no.2 konstanta string

nama = 'iva'
umur = 19
tinggi = 155
print("nama: ", 'umur: ', 'tinggi: ', tinggi) #variabel sederhana

x = 10
print('nilai variabel sebelum diubah: ', x)
x = 20
print('nilai variabel sesudah diubah: ', x) #variabel sederhana

#STATEMENT
'''adalah instruksi atau perintah yg diberikan kpd python agar dikerjakan.
1. assigment statement, memberi nilai pd sebuah variabel. contoh: x=5
2. expression statement, penugasan dmn nilai variabel didapat dri hasil operasi/perhitungan. contoh: c=a+b
3. print/output statement, perintah utk menampilkan teks, angka, atau hasil ekspresi ke layar.
    contoh:'''
print(123)
print("hai")
'''
4. conditional statement, perintah dgn kondisi sprti if, else
5. looping statement, perintah pengulangan.'''
for i in range(1,11):
    print(i)
'''
6. control statement, utk mengontrol jalannya program.'''
'''break, menghentikan loop'''
for i in range (1,7):
    if i==5:
        break #berhenti di angka 5
''' continue, melanjutkan ke iterasi berikutnya'''
for i in range (1,7):
    if i==4:
        continue #skip di angka 4
'''pass, placheholder(tdk melakukan apa-apa)'''
def fitur_baru():
    pass #blm diisi, hanya placeholder
print('\nProgram selesai!')

#EXPRESSION
'''adalah unit sintaksis yg menghasilkan sebuah nilai saat dievaluasi.
1. numeric expression, +, -, /, //(pembagian habis dibulatkan, *(perkalian), **(perpangkatan), %(sisa bagi)
2. operator predence(aturan prioritas): tanda kurung, pangkat, perkalian, pembagian, kiri ke kanan.

LATIHAN'''
satu = 2+3 * 4
print(satu)
dua = 2 ** 3
print(dua)
tiga = (10-2)*3+4
print(tiga)
empat = 20/5 * 2 % 3
print(empat)
lima = (2+3)*2**2-8/2
print(lima)

#TYPE MATTERS
x = 3
print(type(x))

#TYPE CONVERSATION
'''1. integer otomatis menjadi float'''
x=5   #int
y=2.1 #float
hasil= x+y
print('hasil: ', hasil, 'tipe: ', type(hasil))
'''2. mengontrol dgn integer'''
x=5.3
y=2.2
hasil = int(x)+int(y)
print('hasil: ', hasil, 'tipe: ', type(hasil))
'''3. membaca input sbgai string, peraturan default'''
nama = input("masukkan nama bias anda: ")
print('hallo', nama, 'tipe data: ',type(nama))
'''4. konversi input ke float'''
nilai = input('masukkan nilai anda: ')
nilai = float(nilai)
print('nilai anda: ', nilai)

#LIST
'''tipe data didalamny tdk harus sama dan bersifat mutable, dpt diubah nilai/elemennya'''
cortis = ['james','martin','juhoon','sean','keonho']

print('member cortis: ', cortis) #mencetak semua isi dlm list
print('nilai pertama: ', cortis[0]) #mengakses elemen pertama(indeks ke 0)

cortis[0]= "zhao yu fan" #mengubah nilai dlm list
print('nilai setelah diubah: ', cortis)
cortis[1:3]= ['edward', 'juju'] #mengubah nilai dlm range

cortis.append('iva') #menambah hanya bisa satu data
cortis.extend(['vava', 'seonghyeon']) #menambah banyak data
print('daftar setelah ditambah: ', cortis)

cortis.remove('iva') #menghapus data
del cortis[-2]
print('daftar setelah dihapus: ', cortis)
cortis.clear() #menghapus seluruh data dlm list
print('daftar setelah dibersihkan: ', cortis)

'''slicicng list'''
print(cortis[0:4]) #mengambil nilai dri indeks ke 0 sampai sblm 4
print(cortis[0:-1]) #mengambil nilai kecuali yg terakhir
print(cortis[-1:-3]) #slicing terbalik
print(cortis[-3:-1])
'''slicing tanpa batas'''
print(cortis[1:]) #nilai dari indeks ke 1 sampai akhir
print(cortis[:1]) #nilai dari awal sampai sblm 1
'''

LATIHAN'''
print()
print('latihan pertemuan ketiga')

teman = ['siska', 'cika', 'taca', 'bening', 'valen'] #no1
print(teman[0])
print(teman[-1]) #no2
teman[3]='budi'
print(teman) #no3
print(teman.append['iva']) #no4
print(teman.insert['siti']) #no5
del cortis[-1]
print(cortis) #no6
print(cortis.remove['budi']) #no7
print(cortis[0:4]) #no8
print()

'''PERTEMUAN 4 (conditional statement)'''

'''digunakan utk mengeksekusi blok kode tertentu pada kondisi tertentu. seperti if, elif, else'''
#OPERATOR PERBANDINGAN, utk membandingkan 2 niai dan menghasilkan nilai true/false
x = 5
y = 3
print(x == y)
print(x != y) #tdk sama dengan

#OPERATOR LOGIKA, utk menggabungkan conditional statement
'''
1. and, true jika kedua kondisi benar
2. or, true jika salah satu kondisi benar
3. not, membalikkan nilai true dan false'''
print(x>y and x<y)
print(x>y or x<y)
print((not x>3 and x<10))

# IF STATEMENT, akan mengeksekusi jika kondisi bernilai true, mengandalkan indentasi(spasi)
a=22
b=11
if b > a: print('b lebih besar dari a')
'''contoh masalah:'''
bilangan = float(input('masukkan suatu bilangan: '))
if bilangan > 0:
    print('bilangan: ', bilangan, 'adalah bilangan positif.')
elif bilangan < 0:
    print('bilangan: ', bilangan, 'adalah bilangan negatif.')
else:
    print('bilangan tersebut adalah bilangan 0')

