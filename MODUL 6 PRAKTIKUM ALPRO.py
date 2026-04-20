# fungsi faktorial rekursif
def fibonaci(n):
    if n <= 1 or n==2:
        return 0
    else:
        return fibonaci(n-1) + fibonaci(n-2)
    
def main():
    while True:
        bil = int(input('masukkan angka'))
        print(f"fibonaci:({bil})={fibonaci(bil)}")

        lagi=input('cari lagi (y/t)')
        if lagi.lower() != 'y':
            break

if __name__ == "__main__":
    main()
print()

# 2. Menghitung Faktorial
def fact_rec(n):
    """
    Menghitung nilai faktorial dari n secara rekursif.
    """
    # Basis: Faktorial tidak bisa negatif
    if n < 0:
        return 0
    # Basis: 0! dan 1! hasilnya adalah 1
    elif n == 0 or n == 1:
        return 1
    else:
        # Rekurens: n dikalikan dengan faktorial n-1
        return n * fact_rec(n - 1)

def main():
    fac = int(input("Masukkan berapa faktorial: "))
    print(f"Hasil faktorial dari {fac} adalah: {fact_rec(fac)}")

if __name__ == "__main__":
    main()