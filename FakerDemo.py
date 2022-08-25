from faker import Faker

faker= Faker()
for i in range(10):
    print(faker.random.randint(30, 50))
# print("Tam isim: " + faker_it.name())
# print("isim: " + faker_it.first_name())
# print("soyisim: " + faker_it.last_name())
# print("meslek: " + faker_it.job())
# print("adres: "+faker_it.address())


# print("telefon: "+faker.phone_number())

# kisi= faker.profile()
#
# print("dogum tarihi: "+str(kisi.get("birthdate")))
# print("kan grubu: "+str(kisi.get("blood_group")))
#
# print("email: "+ faker.email())
# print("bedava emai: "+ faker.free_email())
# print("sirket email: "+faker.company_email())
#
# print("kredi karti: "+ faker.credit_card_provider())
# print("kredi kart numarasi: "+faker.credit_card_number())
# print("kredi karti guvenlik: "+faker.credit_card_security_code())
# print("kredi karti exp: "+faker.credit_card_expire())
# print("kk full: "+faker.credit_card_full())
