# salam man rasa ansari hastam va in proje class man ast
# ke ba class va taabe init neveshte shode ast 
class Car():
    def __init__(self , berand , nam , modle):
        self.berand = berand
        self.name = nam
        self.modle = modle
LandCruis  = Car('toyota' , 'LandCruis' , 2021)
print(LandCruis.modle)


class Animal():
    def __init__(self2 , nezhad):
        self2.nezhad = nezhad

parande = Animal('aros holandi')
print(parande.nezhad)


class Computer():
    def __init__(self3 , nam2 , berand2):
        self3.nam2 = nam2
        self3.berand2 = berand2
Compu = Computer('Macintosh' , 'apple')
print(Compu.berand2)


class TV():
    def __init__(self4 , berand3):
        self4.berand3 = berand3
tv = TV('LG')
print(tv.berand3)


class Flower():
    def __init__(self5 , no):
        self5.no = no
flower = Flower('rose')
print(flower.no)        
