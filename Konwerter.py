def cels_fahr(temperatura):
    return temperatura * 9/5 + 32

def fahr_cels(temperatura):
    return (temperatura - 32) * 5/9

def m_ft(dlugosc):
    return dlugosc * 3.28084

def ft_m(dlugosc):
    return dlugosc / 3.2808

print("Wybierz konwersję: ")
print("1 : Celsjusz - Fahrenheit")
print("2 : Fahrenheit - Celsjusz")
print("3 : Metr - Stopy")
print("4 : Stopy - Metr")

wynik = input("Twój wybór *wpisz numer*: ")

if wynik == "1":
    temp_c = float(input("Podaj temperaturę w stopniach Celsjusza: "))
    print("Temperatura w stopniach Fahrenheita: ", cels_fahr(temp_c))
elif wynik == "2":
    temp_f = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
    print("Temperatira w stopniach Fahrenheita: ", fahr_cels(temp_f))
elif wynik == "3":
    dl_m = float(input("Podaj długość w metrach: "))
    print("Długość w stopach: ", cels_fahr(dl_m))
elif wynik == "4":
    dl_ft = float(input("Podaj długość w stopach: "))
    print("Długość w metrach: ", fahr_cels(dl_ft))
    