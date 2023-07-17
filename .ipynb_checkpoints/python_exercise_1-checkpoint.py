def one():
    #Pobierz od uzytkownika imie, rok urodzenia i biezacy rok. Nastepni wswietl na konsoli informacje
    #”Witaj! imie, masz wiek uzytkownika lat!

    name = input("Enter a name: ")
    birth_year = int(input("Enter a birth year: "))
    now = int(input("Enter current year: "))

    print(f"Witaj! {name}, masz {now - birth_year} lat!")

def two():
    #Pobierz od uzytkownika dwie liczby i jeden znak. Nastepnie w zaleznosci od znaku wyswietl na konsoli
    #sume/roznice/iloczyn/iloraz tych dwoch liczb.

    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    sign = input('Enter a sign: ')

    if sign == '-':
        c= a - b 
        print(c)
    elif sign == '+':
        c= a + b
        print(c)
    elif sign == '/':
        c= a/b
        print(c)
    elif sign == '*':
        c = a * b
        print(c)


def three():
    #Pobierz od u ̇zytkownika liczbe, nastepnie wypisz czy dana liczba jest parzysta czy nie parzysta.

    l = int(input('Enter a number: '))

    if l == 0:
        print("Liczba zero nie jest podzielna")
    elif l % 2 == 0:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")



def five():
    #Posiadasz pewien zbi ́or liczb okre ́slony przedzialami:
    #A = 〈3, 10)
    #B = (−∞, −17〉
    #C = (5, 140)
    #Sprawd ́z, czy wpisana przez u ̇zytkownika liczba typu float, znajduje sie w tym przedziale. Wynik
    #wypisz na konsole.


    input1 = int(input('Enter a number: '))

    if input1 <= -17:
        print("Liczba mieści się w przedziale B")
    elif input1 >= 3 and input1 < 10:
        print("Liczba mieści się w przedziale A")
    elif input1 > 5 and input1 < 140:
        print("Liczba mieści się w przedziale C")
    else:
        print("Liczba nie mieści się w żadnym przedziale")



if __name__ == '__main__':
    five()