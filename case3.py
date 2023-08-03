class course():
    kursadi = 'Cortex Academy'

    def __init__(self, city):
        self.city = city

class filial(course):

    def __init__(self, city, mekan):
        super().__init__(city)
        self.mekan = mekan

class heyet(filial):

    def __init__(self, city, mekan, ad, ixtisas):
        super().__init__(city, mekan)
        self.name = ad
        self.ixtisas = ixtisas

class koordinat(heyet):

    def __init__(self, city, mekan, ad, ixtisas, maas):
        super().__init__(city, mekan, ad, ixtisas)
        self.maas = maas

class muellim(heyet):
     def __init__(self, city, mekan, ad, ixtisas, worktime):
         super().__init__(city, mekan, ad, ixtisas)
         self.worktime = worktime


class telebe(heyet):
     def __init__(self, city, mekan, ad, ixtisas, bolme, cost ):
         super().__init__(city, mekan, ad, ixtisas)
         self.bolme = bolme
         self.cost = cost

heyet1 = heyet('Baku', 'Nerimanov', 'Kamil', 'koordinator')

koor1 = koordinat('Baku', 'Nerimanov', 'Kamil', 'koordinator', 750)

muellim1 = muellim('Baku', 'Icerisheher', 'Vusal','Cyber-Sec', 'Heftede 10 ders(20 saat)')

telebe1 = telebe('Baku', 'Icerisheher', 'Serxan','IT','Full-stack', '150azn')

print(telebe1.bolme)
        