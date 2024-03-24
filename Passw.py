print("Proszę stworzyć hasło.")
print("Hasło musi zawierać minimum 8 znaków, co najmniej jedną cyfrę i jeden znak specjalny")
haslo = input("Wprowadź swoje hasło: ")
def sprawdz(haslo):
    if len(haslo) < 8:
        return 'Hasło musi zawierać więcej, niż 8 znaków!'
    