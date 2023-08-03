class bilet():
    konsert = 'ARTBAT'
    count = 120

    def __init__(self, biletid, saat, yer, sinif, mekan):
        self.biletid = biletid
        self.saat = saat
        self.yer = yer
        self.sinif = sinif
        self.mekan = mekan

    def sold(self,say=1):
        if (self.count > 0 and say <= 120):
            self.count -= say
            return self.count
        else:
            return f'Teessufki biletler bitib.'
        
    def __repr__(self):
        return f'{self.biletid} {self.saat} {self.yer} {self.sinif} {self.mekan}'
    

        
    
bilet1 = bilet('B235', '00:00', 'Baku', 'adi', 'Crystal Hall' )

print(bilet1.sold())

print(bilet1)

        