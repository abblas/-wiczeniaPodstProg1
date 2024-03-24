print('Kalkulator')


def dodawanie(x,y):
    return x + y

def odejmowanie(x,y):
    return x - y

def mnożenie(x,y):
    return x * y

def dzielenie(x,y):
    return x / y

operacja = input("Wybierz operację (+,-,*,/).")

if operacja in ("+","-","*","/"):
    liczbax = float(input("Podaj pierwszą liczbę."))
    liczbay = float(input("Podaj drugą liczbę.")) 
    
    if operacja == "+":
        print("wynik:", dodawanie( liczbax, liczbay ) )
    elif operacja == "-":
        print("wynik:", odejmowanie( liczbax, liczbay ) )
    elif operacja == "*":
        print("wynik:", mnożenie( liczbax, liczbay ) )
    elif operacja == "/":
        print("wynik:", dzielenie( liczbax, liczbay ) )

        