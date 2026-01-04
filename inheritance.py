class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}"
    
    def nyalakan(self):
        print(f"{self.merek} dinyalakan")

class Mobil(Kendaraan):

    def __init__(self, merek, tahun, jumlah_roda):
        super().__init__(merek, tahun)
        self.jumlah_roda = jumlah_roda

    def klakson(self):
        print(f"Mobile {self.info()} memiliki klakson")

class Motor(Kendaraan):

    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson")

    def nyalakan(self):
        print(f"{self.merek} dinyalakan secara otomatis")

avanza = Mobil("Avanza", 2019, 4)
avanza.nyalakan()
avanza.klakson()
print(avanza.jumlah_roda)

scoopy = Motor("Scoopy", 2022)
scoopy.nyalakan()
scoopy.klakson()


class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class KaryawanTetap(Karyawan):
    pass

class Manager(KaryawanTetap):
    pass

class VicePresident(Manager):
    pass

class BisaBerlari:
    def berlari(self):
        print("Berlari sangat cepat")

class BisaBerenang:
    def berenang(self):
        print("Berenang sangat cepat")

class Atlit(BisaBerlari, BisaBerenang):
    def __init__(self, name):
        self.name = name

eko = Atlit("Eko")
eko.berlari()
eko.berenang()

class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

d = D()
d.method()
print(d.method())

eko = Karyawan("Eko", 10000000)
tono = KaryawanTetap("Tono", 10000000)
budi = Manager("Budi", 10000000)
joko = VicePresident("Joko", 10000000)

print(isinstance(eko, Karyawan))
print(isinstance(tono, Karyawan))
print(isinstance(budi, Karyawan))
print(isinstance(joko, Karyawan))

