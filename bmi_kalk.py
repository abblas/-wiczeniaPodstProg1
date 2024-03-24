
def getbmi(x, y):
    return x/(y*y)
x = float(input("Podaj wagę w kg: "))
y = float(input("Podaj wzrost w m: "))  

bmi = getbmi(x, y)
if bmi < 18.5:
        print("Niedowaga")
elif 18.5 < bmi < 24.9:
        print("Waga prawidłowa")
elif 25 < bmi < 29.9:
        print("Nadwaga")
elif 30 < bmi < 34.9:
        print("Otyłość stopnia pierwszego")
elif 35 < bmi < 39.9:
        print("Otyłość stopnia drugiego")
elif bmi < 40:
        print("Otyłość stopnia trzeciego.")
        