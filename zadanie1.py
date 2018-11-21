# # # # # print("Hello world", '\n', "ssss")
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # tablica = [1,2,'asdfasd']
# # # # # print(tablica[0])  # wypisze 1
# # # # # print(tablica[1])  # wypisze 2
# # # # # print(tablica[2])  # wypisze 3
# # # # #
# # # # # # wypisze kolejno 1, 2, 3
# # # # # for x in tablica:
# # # # #     print(x)
# # # # #
# # # # #
# # # # # fgh = "TTT"*10
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # x = object()
# # # # # y = object()
# # # # #
# # # # # # zmien ten kod
# # # # # x_tab = [x]
# # # # # y_tab = [y]
# # # # # duza_tab = []
# # # # #
# # # # # print("x_tab zawiera %d obiektow") % len(x_tab)
# # # # # print("y_tab zawiera %d obiektow") % len(y_tab)
# # # # # print("duza_tab zawiera %d obiektow") % len(duza_tab)
# # # # #
# # # # # # sprawdzenie poprawnosci
# # # # # if x_tab.count(x) == 3 and y_tab.count(y) == 6:
# # # # #     print("Prawie zrobione...")
# # # # # if duza_tab.count(x) == 3 and duza_tab.count(y) == 3:
# # # # #     print("Doskonale!")
# # # #
# # # # # imie1 = "Marek"
# # # # # imie2 = "Dorota"
# # # # # print("%s ma %s " % (imie1, imie2))
# # # # #
# # # # # imie = "Marek"
# # # # # print("Witaj, %s!") % imie
# # # # # imie = "Dorota"
# # # # # print("Witaj, %s!") % imie
# # # # #
# # # # # # To wypisze "Marek ma 23 lata."
# # # # # imie = "Marek"
# # # # # wiek = 23
# # # # # print("%s ma %d lata." % (imie, wiek))
# # # #
# # # # # # tak tworzymy krotke
# # # # # dane = ("Dorota", 5, 32)
# # # # # print("%s mieszka w bloku nr %d w mieszkaniu %d" % dane)
# # # #
# # # #
# # # # rzeczywista_1 = 4.34
# # # # rzeczywista_2 = 54.432
# # # # calkowita = 160
# # # #
# # # # print("rzeczywista_1 = %f" % rzeczywista_1)
# # # # print("rzeczywista_2 = %f" % rzeczywista_2)
# # # # print("rzeczywista_2 = %.1f" % rzeczywista_2)
# # # # print("W systemie szesnastkowym %d ma postac %X" % (calkowita, calkowita))
# # # #
# # # # print("JJJ KKK LLL \"AAA\".")
# # # #
# # # #
# # # # napis = "AAA BBB ..."
# # # # print(len(napis))  # 11
# # # #
# # # #
# # # # napis = "abcdeabcdeabcde"
# # # # print(napis.count("a"))  # 0
# # # # print(napis.index("d"))  # 3
# # # #
# # # #
# # # # napis = "abcdefghijk"
# # # # print(napis[3:4])  # c
# # # #
# # # #
# # # # napis = "abcdefg"
# # # #
# # # # print(napis[0:4])  # abcd
# # # # print(napis[:4])  # abcd
# # # #
# # # # print(napis[::])  # Wypisze caly napis
# # # #
# # # # # zamiast liczby mozemy podac wyrazenie,
# # # # # ktorego wynikiem jest liczba
# # # # print(napis[4:len(napis)])  # efg
# # # # print(napis[4:])           # efg
# # # #
# # # #
# # # #
# # #
# # #
# # #
# # # napis = "Witaj Alu"
# # # print(napis.startswith("Witaj"))  # True
# # # print(napis.startswith("Czesc"))  # False
# # # print(napis.endswith("Alu"))     # True
# # # print(napis.endswith("swiecie"))  # False
# # #
# # #
# # # napis = "Ala ma kota."
# # # tablica_slow = napis.split(" ")
# # # print(tablica_slow)  # ['Ala', 'ma', 'kota']
# # #
# # #
# # # s = "Jaki powinien byc ten napis?"
# # #
# # # # Powinien byc dlugi na 17 znakow
# # # print("Dlugosc napisu = %d" % len(s))
# # #
# # # # Pierwsza litera 'a' w tekscie powinna miec indeks nr 1
# # # print("Indeks pierwszej litery 'a' = %d" % s.index("a"))
# # #
# # # # W napisie musza byc dwie litery 'a'
# # # print("'a' wystepuje %d razy" % s.count("a"))
# # #
# # # # Dzielenie napisu na kawalki
# # # print("Pierwszych piec znakow to '%s'" % s[:5])
# # # print("Nastepne piec znakow to '%s'" % s[5:10])
# # # print("Dwunastym znakiem jest '%s'" % s[12])
# # #
# # # print("Ostatnie piec znakow to '%s'" % s[-5:])
# # #
# # # # Zamien wszystkie male litery na duze
# # # print("Uzywajac duzych liter: %s" % s.upper())
# # #
# # # # Zamien wszystkie litery na male
# # # print("Uzywajac malych liter: %s" % s.lower())
# # #
# # # # Musi sie zaczynac od "Nap"
# # # if s.startswith("Nap"):
# # #     print("Napis zaczyna sie od 'Nap'. Dobrze!")
# # #
# # # # Sprawdzamy jak konczy sie napis
# # # if s.endswith("tne"):
# # #     print("Napis konczy sie 'tne'. Dobrze!")
# # #
# # # # Rozdziela napis na trzy czesci,
# # # # z ktorych kazda zawiera tylko jedno slowo
# # # print("Napis rozdzielony na slowa: %s" % s.split(" "))
# # #
# # #
# # #
# #
# # imie = "Rober"
# # if imie in ["Jan", "Robert"]:
# #     print("Nazywasz sie Jan lub Robert")
# # elif imie == "T":
# #     print("Jajo")
# # else:
# #     print("Nic")
# #
# #
# #
# #
# # x = [1,2,3]
# # y = [1,2,3]
# # print(x == y)  # Wypisze True
# # print(x is y)  # Wypisze False
# #
# # tablica = [1, 2, 3]
# # tablica2 = ['a', 'b', tablica]
# # print (tablica == tablica2[2])  # True
# # print (tablica is tablica2[2])  # True
# #
# # # Ponizej dowod na to, ze is mowi prawde
# #
# # tablica.append(4) # Dodajemy do tablicy liczbe 4
# # print(tablica2[2])  # [1, 2, 3, 4]
# #
# #
# # # Zmien ponizszy kod
# # liczba = 10
# # druga_liczba = 10
# # pierwsza_tablica = []
# # druga_tablica = [1,2,3]
# #
# # if liczba > 15:
# #     print "1"
# #
# # if pierwsza_tablica:
# #     print "2"
# #
# # if len(druga_tablica) == 2:
# #     print "3"
# #
# # if len(pierwsza_tablica) + len(druga_tablica) == 5:
# #     print "4"
# #
# # if pierwsza_tablica and pierwsza_tablica[0] == 1:
# #     print "5"
# #
# # if not druga_liczba:
# #     print "6"
#
#
#
# # Wypisze liczby 0 1 2 3 4
# for x in range(7,3,-1):
#     print(x)
#
# print('\n')
#
# # Wypisze 3 4 5
# for x in reversed(range(3,8)):
#     print(x)
# print('\n')
#
# licznik = 0
# while licznik < 5:
#     print(licznik),
#     licznik += 1  # Ma to taki sam efekt jak licznik = licznik + 1
#
# print('\n')
# # Wypisze 0 1 2 3 4
#
# licznik = 0
# while True:
#     print(licznik)
#     licznik += 1
#     if licznik >= 5:
#         break
#
# print('\n')
#
# # Wypisze tylko liczby nieparzyste - 1 3 5 7 9
# for x in range(10):
#     # Sprawdz, czy x jest parzyste
#     if x % 2 == 0:
#         continue
#     print(x)
#
#
# liczby = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
#
# # miejsce na twoj kod
#
# for x in liczby:
#     if x >= 237:
#         continue
#     if x % 2 == 0:
#         print(x)
#
#
# def przywitanie():
#     print("Pozdrowienia z mojej funckji!")
#
# def przywitanie_imienne(imie, zyczenia):
#     print("Witaj" + imie + ". Zycze Tobie " + zyczenia)
#
# przywitanie()  # Wypisze "Pozdrowienia z mojej funckji!"
# przywitanie_imienne("Jacek", "zdrowia")  # Wypisze immienne zyczenia
# print('\n')
# def dzielenie(dzielna, dzielnik):
#     if(dzielnik == 0):
#         return # zakoncz funkcje nic nie zwracajac
#     else:
#         return dzielna / dzielnik
#
# print(dzielenie(5, 0))
# print("#########################")
# print(dzielenie(10, 2))
# print("#########################")
# # brak argumentow i zwracanej wartosci
# przywitanie()
#
# # brak zwracanej wartosci, ale sa juz argumenty
# przywitanie_imienne("Jacek", "zdrowia")
#
# # jak przypisac zmiennej wartosc zwrocona przez funkcje
# x = dzielenie(9, 3)
# print(x)
# print("#########################")
# def lista_korzysci():
#     return("Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby")
# def buduj_zdanie(info):
#     return info + " JJJ KKK"
#
# print (buduj_zdanie(lista_korzysci()[2]))
# print("#########################")
# for x in lista_korzysci():
#     print(buduj_zdanie(x))
# print("#########################")
# class MojaKlasa:
#     zmienna = "blah"
#
#     def funkcja(self):
#         print("To jest wiadomość wewnątrz klasy.")
#
# mojobiekt = MojaKlasa()
# print(mojobiekt.zmienna)
# mojobiekt.zmienna = "ple"
# print(mojobiekt.zmienna)
# print("#########################")
# class Czlowiek:
#     imie = ""
#     nazwisko = ""
#     wiek = 0
#     def zwroc(self):
#         print(self.imie,self.nazwisko,self.wiek)
# c1 = Czlowiek()
# c2 = Czlowiek()
#
# c1.imie = "Ania"
# c1.nazwisko = "Kowalska"
# c1.wiek = 111
#
# c1.zwroc()
# print("#########################")
# kontakty = {
#     "Jan": 938477566,
#     "Jacek": 938377264,
#     "Janusz": 947662781,
#     "X" : {"a":3,"b":2}
# }
#
# print(kontakty["X"]["a"])
# print("#########################")
# del kontakty["Jan"]
# kontakty.pop("Jacek")
# for imie, numer in kontakty.items():
#     print("%s ma numer telefonu: %d" % (imie, numer))
# print("#########################")
# from p1 import new1
# from p1.p2 import new2
# kontakty = {
#     "Jan": 938477566,
#     "Jacek": 938377264,
#     "Janusz": 947662781,
#     "X" : {"a":3,"b":2}
# }
# kontakty.update({"Jakub": 15123123, "DDD": 28179123})
# print(kontakty)
# print(new1.f1())
# print(new2.f2())

# napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
# slowa = napis.split() # tworzymy tablice ze slowami zawartymi w napisie
# dlugosc_slow = []
# for slowo in slowa:
#     if slowo != 'nad':
#         dlugosc_slow.append(len(slowo))
#
# print(dlugosc_slow)

# napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
# slowa = napis.split()
# dlugosc_slow = [len(slowo) for slowo in slowa if slowo != 'nad']
#
# print (dlugosc_slow)

# liczby = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#
# nowa = [int(liczby) for liczby in liczby if liczby >=0 ]
#
# print(nowa)
#
# def foo(pierwszy, drugi, trzeci, *reszta):
#     print ("Pierwszy: %s" % pierwszy)
#     print ("Drugi: %s" % drugi)
#     print ("Trzeci: %s" % trzeci)
#     print ("I cala reszta... %s" % list(reszta))
#
#
# print (foo(1,2,3,4,5,6,7,8))

# def funkcja(pierwszy, drugi, trzeci, **opcje):
#     if opcje.get("akcja") == "dodaj":
#         print ("Suma to: %d" % (pierwszy + drugi + trzeci))
#
#     if opcje.get("zwroc") == "pierwszy":
#         return pierwszy
#
# wynik = funkcja(1, 2, 3, akcja = "dodaj", zwroc = "pierwszy")
# print ("Wynik: %d" % wynik)

# zmien funkcje ponizej
# def foo(a, b, c, *d):
#     return len(d)
#
# def bar(a, b, c, **opcje):
#     if opcje.get("magiczna_liczba") ==7:
#         return True
#     else:
#         return False
#
#
# # test kodu
# if foo(1,2,3,4) == 1:
#     print ("Dobrze.")
# if foo(1,2,3,4,5) == 2:
#     print ("Lepiej.")
# if bar(1,2,3,magiczna_liczba = 6) == False:
#     print ("Bardzo dobrze.")
# if bar(1,2,3,magiczna_liczba = 7) == True:
#     print ("Doskonale!")
#
# import re
#
# tekst = """1234 5431 Wyobraz sobie, ze ten tekst zawiera numer PIN 9431 twojej karty do bankomatu, a ty wlasnie go
# zapomniales. Jak szybko go odnalezc 1234?"""
#
# sciezka = r'\d\d\d\d.*?9'
# dopasowanie = re.search(sciezka, tekst)
#
# if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
#     numer = dopasowanie.group()
#     print (numer)

# przyklad
# import re
# # Ponizej jest dokonywana lekka optymalizacja naszego wyrazenia
# pattern = re.compile(r"\[(on|off)\]")
#
# # Teraz szukamy
# re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
# # Zwroci obiekt Match
# re.search(pattern, "Nada...:-(")
# # Nic nie zwroci
# # koniec przykladu
#
# # Cwiczenie: skonstruj wyrazenie odpowiadajace adresowi email
#
# def test_email(twoje_wyrazenie):
#     wyrazenie = re.compile(twoje_wyrazenie)
#     adresy = ["john@example.com", "python-list@python.org", '"wha.t.`1an?ug{}ly@email.com"']
#     for adres in adresy:
#         if not re.match(wyrazenie, adres):
#             print ("Nie udalo ci sie przyporzadkowac %s" % (adres))
#         elif not twoje_wyrazenie:
#             print ("Nie wprowadziles wyrazenia do funkcji test_email")
#         else:
#             print ("Dobrze")
#
# wyrazenie = r".*?@.*?" # Tu wpisz swoje wyrazenie
# test_email(wyrazenie)

# tab = [1,2,3]
# for i in range(10):
#     try:
#         print(tab[i])
#     except IndexError: # Raised when accessing a non-existing index of a list
#         print("Źle")

# #Obsluz wszystkie wyjatki
# # aktor = {"imie": "Piotr Fronczewski", "opinia": "swietny"}
# #
# # #Musisz ta funkcje zmodyfikowac tak, aby zwracala nazwisko aktora.
# # # W razie potrzeby przypomnij sobie poprzednie lekcje
# # def zwroc_nazwisko():
# #     try:
# #         nazwisko = aktor["imie"].split()[1]
# #         return nazwisko
# #     except:
# #         return "Błąd"
# #
# # #Test kodu
# # zwroc_nazwisko()
# # print ("Wszystkie wyjatki obsluzone! Dobra robota!")
# # print ("Nazwisko aktora brzmi %s" % zwroc_nazwisko())

# print (set("jego imie to Eryk i Eryk jest jego imieniem".split()))

# A = set(["Jake", "John", "Eric"])
# B = set(["John", "Jill"])
# #
# # print (A.intersection(B)) # set(['John'])
# # print (B.intersection(A)) # set(['John'])
#
# print (A.symmetric_difference(B)) # set(['Jill', 'Jake', 'Eric'])
# print (B.symmetric_difference(A)) # set(['Jill', 'Jake', 'Eric'])
#
# print (A.difference(B)) # set(['Jake', 'Eric']
# print (B.difference(A)) # set(['Jill'])
#
# print (A.union(B)) # set(['Jill', 'Jake', 'John', 'Eric'])
#
# tablica_a = ['Anna', 'Monika', 'Joanna', 'Ewa', 'Karolina', 'Kacper', 'Dawid', 'Mateusz', 'Ewa', 'Bartosz']
# tablica_b = ['Kuba', 'Paulina', 'Marzena', 'Zuza', 'Tomek', 'Ewa', 'Bartek', 'Olek', 'Jacek', 'Magda', 'Paulina']
# tablica_c = ['Anastazja', 'Ewa', 'Monika', 'Anna', 'Karolina', 'Ola', 'Ula', 'Maciek', 'Paulina']
#
# A = set(tablica_a)
# B = set(tablica_b)
# C = set(tablica_c)
#
# print (A.union(B,C))
# print (A.intersection(B,C))
# print (A.symmetric_difference(B.union(C)))

# from functools import partial
#
# def mnozenie(x, y, z):
#     return x * y * z
#
# podwojenie = partial(mnozenie, 2, 2)
#
# print (podwojenie(6))  # 12
# print (podwojenie(11))  # 22
# print (podwojenie(7))  # 14

import django

