class user():

    def __init__(self, ad , soyad , tel) :
      
        self.name = ad 
        self.surname = soyad
        self.tel = tel

   

    def id_generate(self):
        return self.name[:3].lower()+self.surname[-3:].lower()+self.tel[-4:].lower()

user1 = user('Serxan', 'Elili', '0505505001')

user2 = user('Orxan', 'Babayev', '0552304550')

user3 = user(ad = input('Ad: '), soyad = input('soyad: '), tel = input('tel: '))

print(user1.id_generate())