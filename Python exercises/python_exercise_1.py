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


def six():
    #Korzystając z petli napisz program ktory:
    #wypisze na konsole liczby od 1 do 10 

    #for i in range(0,11):
        #print(i, ' ', end ='')

    #for i in reversed(range(0,11)):
       # print(i, ' ', end ='')

    #for i in range(10,1,-1):
        #print(i, ' ', end ='')

    for i in range(10,42,2):
        print(i, ' ', end ='')

def seven():
    #Stworz petle, w ktorej uzytkownik moze wpisac 5 razy jakies wartosci. Na koniec programu wypisz
    #sume liczb wpisanych przez uzytkownika.
    
    count = 0 
    suma = 0
    while count < 5:
        count = count +1
        user = int(input("Enter a number: "))
        suma = suma + user
    print(suma) 

def eight():
    #Stworz program pobierajacy dwie liczby od uzytkownika (a i b). Nastepnie korzystajac z petli oblicz
    #wartosc potegi liczby a podniesionej do liczby b.

    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print(a**b)

def nine():
    #Napisz program, ktory w petli prosi uzytkownika o wpisanie dodatniej liczby calkowitej; wczytywanie
    #konczy sie, gdy uzytkownik poda liczbe 0. Nastepnie program wypisuje te z wczytanych liczb, dla
    #ktorej suma cyfr jest najwieksza (oraz te sume cyfr).

    lista = []
    max_suma = 0
    max_number = 0
    num = input("Enter a number: ")
    lista.append(num)
    while int(num) > 0:
        num = input("Enter a number: ")
        lista.append(num)
    for wyraz in lista:
        suma = 0 
        for i in wyraz:
            suma += int(i)
        if suma > max_suma:
            max_suma = suma
            max_number = wyraz
    print(f' Maksymalna suma to: {max_suma}, maksymalna liczba to: {max_number}')

def nine_half():
    #Napisz program, ktory w petli prosi uzytkownika o wpisanie dodatniej liczby calkowitej; wczytywanie
    #konczy sie, gdy uzytkownik poda liczbe 0. Nastepnie program wypisuje te z wczytanych liczb, dla
    #ktorej suma cyfr jest najwieksza (oraz te sume cyfr).

    lista = []
    min_suma = 10000
    min_number = 0
    num = input("Enter a number: ")
    while int(num) > 0:
        lista.append(num)
        num = input("Enter a number: ")
    for wyraz in lista:
        suma = 0 
        for i in wyraz:
            suma += int(i)
        if suma < min_suma:
            min_suma = suma
            min_number = wyraz
    print(f' Minimalna suma to: {min_suma}, minimalna liczba to: {min_number}')

def ten():
    #Pobierz trzy liczby z klawiatury. Nastepnie wpisz w konsole "histogram" tych liczb, stworzony ze znaków spacji i gwiazdek. Np dla liczb 4,1,2 na konsoli powinien 
    # pojawić się napis:
# *
# *
# * *
# ***

    lista = []
    max_input = 0
    for i in range(3):
        a = int(input('Enter a number: '))
        lista.append(a)
        if a > max_input:
            max_input = a 
    for row in range(max_input,0,-1):
        #i=4 
        for column in range(3):
            if lista[column] >= row:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()

def eleven():
    #Trójkąt
    for i in range(5):
        print((i+1) * '*')

def twelve():
    #Odwrócony trójkąt
    for i in range(6,0, -1):
        print((i-1) * '*')

def thirteen():
    #Stwórz liste różnych imion, nastepnie stworz program, ktory będzie usuwał z listy imiona które zostaną wpisane przez użytkownika na konsoli. 

    lista_imion = ['Eustachy', 'Mateusz', 'Genowefa', 'Sebastian', 'Ania', 'Daria', 'Tomek', 'Karol']


    imie_input = input('Enter a name to delete: ')
    imie_skasowane = False
    for i in lista_imion:
        if imie_input == i:
            lista_imion.remove(i)
            imie_skasowane = True
            print('Imie zostało skasowane')
    if not imie_skasowane:
            print('Nie ma takiego imienia w liście')
    print(lista_imion)

def fourteen():
    #Stwórz listę przechowującą różne instrumenty w orkiestrze. Napisz program który zliczy ile razy w liście pojawie się instrument "Violin"

    lista_imion = ['Eustachy', 'Mateusz', 'Genowefa', 'Sebastian', 'Ania', 'Daria', 'Tomek', 'Karol', 'Karol', 'Eustachy', 'Sebastian', 'Sebastian', 'Sebastian', 'Sebastian', 'Genowefa']

    count_eust = 0
    for i in lista_imion:
        if i == 'Eustachy':
            count_eust += 1
    print(f'Imię Eustachy pojawia się w liście {count_eust} razy')
    print(lista_imion.count('Sebastian'))

def fifteen():
    #Stworz liste oraz wypełnij ja 10-cioma losowymi liczbami, nastepnie napisz program ktory uporządkuje te liczby rosnąco. Wpisz tablice w nowym porzadku.

    lista_liczb = [24353, 25, 1000000, 444, 23, 99999, 6666666, 45, 60, 1000]

    size = len(lista_liczb)

    print("Before sorting:", lista_liczb)

    for i in range(size):
        for j in range(0, size-1):
            if lista_liczb[j] > lista_liczb[j+1]:
                tmp = lista_liczb[j]
                lista_liczb[j] = lista_liczb[j+1]
                lista_liczb[j+1] = tmp
                #lista_liczb[j], lista_liczb[j+1] = lista_liczb[j+1], lista_liczb[j]
                print(lista_liczb)

    print("After sorting:", lista_liczb)

def sixteen():
    dict = {"origin": "Warsaw",
    "destination": "Helsinki",
    "time": 1.4,
    "number": "F679"}

    for key in dict.keys():
        print(key)
    for value in dict.values():
        print(value)

def seventeen():
    dict_user = {}
    for i in range(3):
        input_key = input("Wprowadź dowolny klucz: ")
        input_value = input("Wprowadź dowolną wartość: ")
        dict_user[input_key] = input_value
        
    if 'model' in dict_user:
        print(dict_user['model'])
    else:
        print("Brak klucza w słowniku")

def eighteen():
    dict = {'Harry Potter i Więzień Azkabanu': {'Autor': 'J.K.Rowling',
                                                'Rok wydania': 2010,
                                                'Numer isbn': 635574457745},
            'Harry Potter i Komnata Tajemnic': {'Autor': 'J.K.Rowling',
                                                'Rok wydania': 2015,
                                                'Numer isbn': 5345435345345},
            'Zielona Mila': {'Autor': 'Stephen King',
                            'Rok wydania': 2011,
                            'Numer isbn': 5353453453}
            } 

    
    input_user = input('Wpisz wybranego autora: ') 
    lista_ksiazek = []
    for i in dict.keys(): #printuje tytuly
        #print(dict[i]['Autor']) #printuje wszystkich autorow
        if input_user == dict[i]['Autor']:
            lista_ksiazek.append(i)
        else:
            print('Nie mamy takiego autora')
    print(lista_ksiazek)
           


class Trzyde:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def getDistance(self, point_b):
        punkt = point_b - self.x
        return punkt


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def isInside(self, point_p):
        pass

    def distanceFromEdge(self, point_p):
        pass

    def expand(self, val):
        nowe_a = val + self.a
        nowe_b = val + self.b
        print(f'Wymiar a wynosi: {nowe_a}, Wymiar b wynosi {nowe_b}')

    def reduce(self, val):
        if val > self.a or val > self.b:
            print('Nie można zmniejszyć figury do zera. Zmniejsz wartość')
        else:
            nowe_a = self.a - val
            nowe_b = self.b - val
            print(f'Wymiar a wynosi: {nowe_a}, Wymiar b wynosi {nowe_b}')

    def getArea(self):
        pole = self.a * self.b
        print(f'Pole wynosi {pole}')

    def getCircum(self):
        obwod = self.a + self.b
        print(f'Obwod wynosi {obwod}')

class Czworobok:
    def __init__(self, x:Punkt, y:Punkt, z:Punkt, h:Punkt):
        self._x = x
        self._y = y
        self._z = z
        self.set_h(h)

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def set_h(self, h):
        if isinstance(h, Punkt):
            self._h = h
        else:
            print('Nie należy do klasy Punkt')
        

    def __str__(self):
        return f"Punkty: {self._x},{self._y},{self._z},{self._h}"

    



if __name__ == '__main__':
    pierwszy_punkt = Punkt(5,10) #dlugosc 10 a
    drugi_punkt = Punkt(1,10) # dlugosc 10 a
    trzeci_punkt = Punkt(5,1) # dlugosc 5 b 
    czwarty_punkt = Punkt(1,1) # dlugosc 5 b 

    obiekt = Czworobok(pierwszy_punkt,drugi_punkt,trzeci_punkt,czwarty_punkt)
    obiekt = Czworobok(1,2,3,4)
    obiekt.set_h(5)
    print(obiekt)
    print(pierwszy_punkt)


    #eighteen()
    #obiekt = Trzyde(10,15,20) 
    #obiekt.getDistance(50)
    #figura = Prostokat(50,30)
    #figura.reduce(20)
    #figura.getArea()
    #figura.getCircum()

