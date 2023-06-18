from django.http import JsonResponse
from fake_data.models import User
import random
from faker import Faker

fake = Faker('pl_PL')
def generate_fake_data(request):
    if (bool(random.randint(0,1))) :
        User.imie = fake.first_name_male()
        User.drugie_imie = fake.first_name_male()
        User.nazwisko = fake.last_name_male()
    else :
        User.imie = fake.first_name_female()
        User.drugie_imie = fake.first_name_female()
        User.nazwisko = fake.last_name_female()
    User.email = fake.email()
    User.telefon = fake.phone_number()
    User.pesel = fake.pesel(date_of_birth=None, sex=None)
    User.ulica = fake.street_address()
    User.miejscowosc = fake.city()
    User.kod_pocztowy = fake.postalcode()
    User.wojewodztwo = fake.administrative_unit()
    User.tablica_rejestracyjna = fake.license_plate()
    User.iban = fake.iban()
    User.firma = fake.company()
    User.regon = fake.regon()
    User.data_urodzin = fake.date()
    User.ipv4 = fake.ipv4()
    User.ipv6 = fake.ipv6()
    User.praca = fake.job()
    User.nip = fake.company_vat()

    return JsonResponse({'imie': User.imie, 
                         'drugie imie': User.drugie_imie,
                         'nazwisko': User.nazwisko,
                         'email': User.email,
                         'numer telefonu': User.telefon,
                         'pesel': User.pesel,
                         'ulica': User.ulica,
                         'miejscowosc':User.miejscowosc,
                         'kod_pocztowy':User.kod_pocztowy,
                         'tablica_rejestracyjna':User.tablica_rejestracyjna,
                         'miedzynarodowy_numer_rachunku_bankowego': User.iban,
                         'firma':User.firma,
                         'praca':User.praca,
                         'regon': User.regon,
                         'nip':User.nip,
                         'data_urodzin':User.data_urodzin,
                         'ipv4':User.ipv4,
                         'ipv6':User.ipv6}, 
                         safe=False, 
                         json_dumps_params={'ensure_ascii': False})
