#modul 1
nama="vava"
print("hallo "+ nama +" cantik, yuk mulai belajar. Fighting!")

greeting="hello world!" #assigment
print(greeting)

#input dan output
nama = input('masukan nama anda:')
print(nama)

#comen, menggunakan awalan simbol pagar #
#block comment, menggunakan 3 double quote atau single quote
'''
ini adalah block comment
teks akan diabaikan oleh python
'''
print()

#modul 2
age=19
salary=500.0
print(type(age))
print(type(salary))

#tipe data primitif numbers
x=22
print(type(x))
x="22"
print(type(x))
x = 1+2j
print(type(x))

#data numbers bersifat immutable
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

#tipe data boolean
x = True
print(type(x))
x = False
print(type(x))

#string
x = 'Dicoding'
print(type(x))

multi_line='''hallo iva!
aku mau jadi data scientist yang hebat!
aku akan selalu rajin belajar!
fighting!'''
print(multi_line)

x = 'Dicoding'
print(x[0])

'''tidak dapat mengubah substring didalammya, karena python bersifat immutable
x = 'Dicoding'
x[0] = 'F'
Output:
TypeError: 'str' object does not support item assignment'''

#metode slicing
x = 'Dicoding'
print(x[2:])

#formated string
name = "Martin Edward"
print(f"Hello, nama saya {name}")

#%-formatting
name = "sean"
print("Nama saya %s" % (name))
print()

#list
x = [1, 2.2, 'Dicoding']
print(type(x))
print()

#Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0
x = [1, 'Dicoding', True, 1.0]
print(x[2])
print()

#list python bersifat mutable
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

#konsep indexing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
print()

'''konsep slicing;sequence[start:stop:step]
start, indeks pertama, inklusif dmn batas akhir yg ditentukan menjadi bagian interval
stop, indeks terakhir, inklusif dmn batas akhir yg ditentukan tidak menjadi bagian interval
step, indeks dmn jumlah elemen yg ingin dilewati antara tiap elemen slice
'''
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2])
print(x[1:])
print(x[:3])
print()

#jenis tipe data collection:tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
#indexing dan slicing
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])
#tuple bersifat immutable
'''input
x = (5, 'program', 1+3j)
x[1] = 'Dicoding'

Output:
'tuple' object does not support item assignment
'''
print()
#set, bersifat unordered collection
'''input
x = {1,2,7,2,3,13,3}
print(x[0])
Output:
'set' object is not subscriptable
'''
#set, bersifat tidak menduplikasi data
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))
print()

#method union (gabungan) dan intersection (irisan)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)
print("union;",union)
print("intersection:",intersection)
print(f"intersection: {intersection}")
print("intersection: "+ str(intersection))
print()

#dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x ['name'])
#menambahkan data cukup dengan memasukan key dan valuenya
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = 'Web Developer'
print(x)
#menghapus data pada dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']
print(x)
#mengubah nama pada dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['name'] = 'james'
print(x)
print()

#konversi tipe data : konversi integer ke float
print(float(5))
#konversi float ke integer
print(int(5.6))
#konversi dari-dan-ke string
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
#konversi kumpulan data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
#konversi ke dictionary
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))

#KUIS
firstName = "vava"
lastName = "aulia"
age = 19
isMarried = False
print(firstName)
print(lastName)
print(age)
print(isMarried)
print()

data_diri = {'firstName':'martin', 'lastName':'edward', 'age':18, 'isMarried':False}
print(data_diri)
print()

#sub modul:Transformasi Angka, Karakter, dan String
#mengubah huruf kecil atau besar
kata = 'dicoding'
kata = kata.upper()
print(kata)
kata = 'DICODING'
kata = kata.lower()
print(kata)
#awalan dan akhiran whitespace
print("Dicoding          ".rstrip())
kata = "vava        "
kata = kata.rstrip()
print(kata)
print("           Dicoding".lstrip())
kata = "    james"
kata = kata.lstrip()
print(kata)
kata = "     vava        "
kata = kata.strip()
print(kata)
print()
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))
print("codecodejamescode".strip("code"))
print()

'''Metode startswith() bertujuan untuk menemukan suatu kata pada awal string
Metode ini mengembalikan nilai True
'''
print('Dicoding Indonesia'.startswith('Dicoding'))
print('Dicoding Indonesia'.startswith('vava'))
#endswith()
print('Dicoding Indonesia'.endswith('Dicoding'))
print('Dicoding Indonesia'.endswith('vava'))

#memisah dan menggabung string
#join()
print(' '.join(['Pretty','Girls','Like','James']))
print('22'.join(['Pretty','Girls','Like','James']))
#split(), kebalikan dari join
print('i love james'.split())
#newline (\n) 
print('''martin,
james,
juhoon,
sean,
keonho.'''.split('\n'))
print()

#replace
string='i love james'
print(string.replace('james','martin'))
#isupper
kata='JAMES'
print(kata.isupper())
#islower
kata='juhoon'
print(kata.islower())
#isalpha
kata='keonho'
print(kata.isalpha())
#isalnum
kata='sean123'
print(kata.isalnum())
print()
#isdecimal
kata='123'
print(kata.isdecimal())
print('123'.isdecimal())
print()
#isspace
print('  '.isspace())
#istitle
print('Sean Cakep'.istitle())

'''Formating pada string
zfill, nambah nilai 0
'''
teks = 'seann'
tambah_number = teks.zfill(6)
print(tambah_number)
#rjust, rata kanan
print('Dicoding'.rjust(20))
#ljust, rata kiri
print('Dicoding'.ljust(20))
#center, rata tengah
print('Dicoding'.center(20,'-'))
print()

#string literals
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
#raw string, mencetak apapun yg kt tulis
print(r'vava22\t')
print()

#operasi pada list, set dan string
x=[1,3,5,6,8,6,7]
print(len(x))
x=set([4,7,5,2,1,3])
print(len(x))
x='belajar'
print(len(x))
#minimal dan maksimal
x=[2,3,4,6,9,1]
print(min(x))
print(max(x))
#count, mencari berapa kali suatu elemen muncul
x=[2,2,3,4,6,6,7,6]
print(x.count(6))
print()
string='belajar yang rajin'
substring='a'
print(string.count(substring))
#in dan not in, memastikan suatu elemen terdapat didalam string
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

#memberi nilai untuk multiple variabel
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)
print()

#sort, mengurutkan huruf kapital, abjad huruf, atau angka, tp tdk bisa alfanumerik
kendaraan = ['Motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

kendaraan = ['motor', 'helikopter', 'pesawat']
print(sorted(kendaraan))

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)

'''Anda dapat memasukkan keyword "str.lower"
pada parameter metode sort()
Jadi, sort() akan menganggap semua objek 
menggunakan huruf kecil, tanpa mengubah kondisi asli objek
'''
kendaraan = ['Motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)
print()

#kuis
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

# TODO: Buat kode Anda di bawah ini
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]
panjang=len(var_list)
maksimal=max(var_list)
minimal=min(var_list)
banyak=var_list.count(605132)

#modul 3: ekspresi
x = 10
y = 2
result = x - y
print(result)

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

learn=['i','v','a']
replikasi=learn*2
print(replikasi)

#ekspresi menurut arity
a = True
a = not a
print(a)
b = 6
b -= 1
print(b)
c = 6
c += 1
print(c)
d = 10
print(-d)

#Ekspresi Menurut Tipe Data yang Dihasilkan
print(2+2)
print(3<10)
print(True or False)
print()

#1. operator aritmatika
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

'''2. Operator relasional, merupakan operator 
perbandingan antara dua operan yang berupa 
integer, float, string, ataupun boolean
Hasil akhir dari operator ini adalah 
nilai bertipe boolean.'''
#Asumsikan kedua variabel bertipe numerik atau float dengan x bernilai 5 dan y bernilai 10.
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Asumsikan x bernilai "Dicoding" dan y bernilai "Indonesia".
x = "Dicoding"
y = "Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

'''3. operator logika
Operator logika merupakan jenis operator 
untuk melakukan operasi logika dengan 
kedua operannya bertipe boolean
Hasil akhir dari operasi ini adalah 
nilai bertipe boolean'''
#asumsikan bahwa p bernilai True dan q bernilai False
print(True and False)
print(True or False)
print(not True)
print(not False)
'''4. operator assigment
pemberian nilai pada suatu variabel dengan nilai tetap'''
x=11
x+=5
print(x)
x=11
x-=5
print(x)
x=11
x*=5
print(x)
x=11
x/=5
print(x)
x=11
x%=5
print(x)
x=11
x=x+5
print(x)
print()

#kuis
'''Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".
'''
total_harga = 750000 - (750000*0.1)
print(total_harga)

'''modul 4
1. Pengenalan Aksi Sekuensial
Pengenalan Aksi Sekuensial
contoh jika urutan baris diubah, mengubah hasil eksekusi
'''
print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
print(umur)
print()

'''contoh jika urutan baris diubah, TIDAK mengubah hasil eksekusi'''
a = 6
b = 9
result = a + b
print(result)

a = 9
b = 6
result = a + b
print(result)

'''2. python interpreter'''
#block code
for i in range(10):
    print(i)
#case sensitive
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)

'''3. one liner'''
#metode secara umum
x = 1
y = 2
temp = x
x = y
y = temp
print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

#metode secara one liner
x = 1
y = 2
x, y = y, x    # One-liner
print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)

'''percabangan dan ternary operator'''
#1. percabangan
ketersediaan = "Daging ayam"
if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

#if
score = 100
if score == 100:
    print("Nilai Anda sempurna!")
#if versi one liner
score = 100
if score == 100:
    print("Nilai Anda sempurna!")

#else, solusi jika kondisi if bernilai false
tinggi_badan = 120
if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

#elif, posisinya berada setelah if dan barisnya tdk dibatasi
nilai = 65

if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")

#or atau 'and'
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

'''2. ternary operators, versi one liner if dan else '''
lulus = True
print("selamat") if lulus else print("perbaiki")
print()
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

#implementasi ternary tuples 
lulus=True
kelulusan=('perbaiki','selamat')[lulus]
print(kelulusan)
print()

'''perulangan
1. for'''
var_list=[1,2,3,4]
for i in var_list:
    print()

for i in range(10):
    print(i)

for i in range(1,13,3):
    print(i)
#while
counter = 2
while counter <= 5:
    print(counter)
    counter += 2
print()

#for bersarang
for i in range(1, 3):
    for j in range(1, 4):
        print(i,j)

#break
for i in range(1,3):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(1,10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 2:
            break 
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
#continue, mengabaikan statement pada continue
for huruf in 'se an':
    if huruf == 'n':
        continue
    print('Huruf saat ini: {}'.format(huruf))
#else setelah for
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")
#else setelah while
count = 0

while count <2:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

#pass
'''x=10
if x >5
  pass
else:
    print('nilai x tidak memenuhi kondisi')
output: tidak menampilkan apapun'''

#list comprehension
angka=[2,3,4]
pangkat=[n**2 for n in angka]
print(pangkat)

#kuis
evenNumber=[i for i in range(0,501,2)]
print(evenNumber)
print()

#modul 6
#fundamental array
import array

x = array.array("d",[1.2, 3.4, 5.4])
print(x)
print(type(x))
print()

var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

#cara mendeklarasikan array
#1. mendefinisikan isi array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)
'''2. mendifinisikan nilai default
Pada materi List Comprehension, kita menggunakan ekspresi.
Namun pada array kita menggunakan default value atau <default-val>'''
vava = [0 for i in range(10)]
print(vava)
'''mengubah nilai default tersebut dengan nilai yang baru
berdasarkan hasil suatu operasi'''
var_arr = [0 for i in range(10)]
for j in range(10):
    var_arr[j] = j
print(var_arr)
print()

#mengakses elemen array
vava=[2,2,1,0,6]
print(vava[0])
#pemrosesan sekuensial pada array
nilai_mahasiswa=[90,80,95,85]
total_nilai=0
for nilai in nilai_mahasiswa:
   total_nilai=total_nilai+nilai
rata_rata=total_nilai/len(nilai_mahasiswa)
print(f'Total Nilai:{total_nilai}')
print(f'Rata-rata Nilai:{rata_rata}')

#mencari nilai terbesar dalam array
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)
print()

#kuis
# Jangan ubah kode ini
var_array = [i for i in range(101)]
# TODO: Silakan buat kode Anda di bawah ini.
total_nilai=0
for i in var_array:
  total_nilai+=i
rata_rata=total_nilai/len(var_array)
result=rata_rata
print(result)
print()

'''modul 7 (matriks)
1. fundamental matriks'''
matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matriks)

#numpy
import numpy
matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)
import numpy as iva
martin = iva.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(martin)
print()

#2. implementasi matriks pada python
matriks = [[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          [0,0,0,1]]
print(matriks)

matriks = [[1 for j in range (4) for i in range (4)]]
print(matriks)
#akses elemen matriks
print(matriks[0][1])

#mengalikan elemen matriks dgn konstanta
import numpy as james
vava = james.array([[2,2,1],
                    [1,1,0],
                    [0,6,6]])
martin = vava*2
print(martin)
print()

'''modul 8 subprogram
1. definisi subprogram''' 
