def klas_wiek(wiek):
    if wiek < 13: 
        return print("Jesteś dzieckiem.")
    elif 13 < wiek < 19:
        return print("Jesteś nastolatkiem.")
    elif 20 < wiek < 65:
        return print("Jesteś dorosły.")
    else:
        return print("Jesteś seniorem.")
    

wiek = int(input("Podaj swój wiek: "))
print(klas_wiek(wiek))

    
    