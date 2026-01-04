class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        print(f"{self.nama} bersuara")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} guk guk")

class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} meow")

class Sapi(Hewan):
    def suara(self):
        print(f"{self.nama} mooo")

hewan_list = [
    Anjing("Anjing"),
    Kucing("Kucing"),
    Sapi("Sapi")
]

for hewan in hewan_list:
    hewan.suara()


class Mobil:
    def start(self):
        print("Mobil berjalan")

class Motor:
    def start(self):
        print("Motor berjalan")

class Perahu:
    def start(self):
        print("Perahu berjalan")

def operasikan_kendaraan(kendaraan):
    kendaraan.start()

kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)

class Apple:
    def __init__(self, jumlah):
        self.jumlah = jumlah
    
    def __add__(self, other):
        return Apple(self.jumlah + other.jumlah)
    
    def __str__(self):
        return f"Apple {self.jumlah}"
    
apple1 = Apple(10)
apple2 = Apple(20)
apple3 = apple1 + apple2

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
       self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shape_list = [
    Rectangle(10, 20),
    Circle(10)
]

for shape in shape_list:
    print(shape.area())