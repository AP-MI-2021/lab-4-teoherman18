def citire_lista():
    """
    Citeste lista
    :return:
    """
    lst = []
    given_string = input("Dati lista, cu elementele separate prin virgula: ")
    numbers_as_string = given_string.split(",")
    for x in numbers_as_string:
        lst.append(int(x))
    return lst

def afisare_lista(lst):
    """
    Afiseaza lista dupa eliminarea duplicatelor
    :param lst: lista de numere intregi
    :return: lista modificata
    """
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


def test_afisare_lista():
    assert afisare_lista([12,13,141]) == [12,13,141]
    assert afisare_lista([]) == []
    assert afisare_lista([12,15,12,155,18,20,12,15]) == [12,15,155,18,20]

def suma_primelor_n_numere_pozitive(lst,n):
    """
    Calculeaza suma primelor n numere pozitive din lista
    :param lst: lista de numere intregi
    :param n: numarul citit de la tastatura
    :return: suma primelor n numere pozitive din lista
    """
    suma = 0
    for i in lst:
        if i >= 0 and n != 0:
            suma = suma + i
            n = n-1
    return suma


def test_suma_primelor_n_numere_pozitive():
    assert suma_primelor_n_numere_pozitive([2,3,4,5,-2,-1],3) == 9
    assert suma_primelor_n_numere_pozitive([0,2,3,-1,5],3) == 5
    assert suma_primelor_n_numere_pozitive([2,3,0,-1,-2],4) == 5

def ordine_crescatoare(lst):
    """
    Verifica daca toate elementele din lista sunt in ordine crescatoare
    :param lst: lista de numere intregi
    :return: True, daca toate elementele din lista sunt in ordine crescatoare, False in caz contrar
    """
    copie = []
    for i in lst:
        if i >= 0:
            copie.append(i)
    for j in range(len(copie)-1):
        if lst[j] > lst[j+1]:
            return False
    return True

def test_ordine_crescatoare():
    assert ordine_crescatoare([12,13,14,15]) is True
    assert ordine_crescatoare([17,16,15]) is False

def numar_divizori(n):
    div = 0
    contor = 2
    while contor < n:
        if n%contor == 0:
            div = div +1
        contor = contor +1
    return div


def alta_lista(lista1):
    """
    Afișarea listei obținute din lista inițială în care numerele care apar doar o singură dată sunt
    nlocuite cu numărul de divizori proprii ai numărului.
    :param lista1: lista nr intregi
    :return: rezultat
    """
    lista2 = []
    for i in range(len(lista1)):
        ok = 1
        for j in range(len(lista1)):
            if lista1[i] == lista1[j] and i != j:
                ok = 0
        if ok == 1:
            lista2.append(numar_divizori(lista1[i]))
        else:
            lista2.append(lista1[i])
    return lista2
def test_alta_lista():
    assert alta_lista([25,13,13,19]) == [1,13,13,0]
def Print_Menu():
    print('1. Citire lista')
    print('2. Afiseaza lista dupa eliminarea duplicatelor')
    print('3. Calculeaza suma primelor n numere pozitive din lista')
    print('4. Verifica daca toate elementele din lista sunt in ordine crescatoare')
    print('5. Listea obținute ')
    print('x. Iesire')


def main():
    test_afisare_lista()
    test_suma_primelor_n_numere_pozitive()
    test_ordine_crescatoare()

    test_alta_lista()
    l = []
    while True:

        Print_Menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(afisare_lista(lst))
        elif optiune == "3":
            n=int(input('Dati numarul: '))
            suma_primelor_n_numere_pozitive(lst,n)
            if n > 0:
                print('Dimensiunea listei este prea mica')
            elif suma_primelor_n_numere_pozitive(lst,n) != 0:
                print(suma_primelor_n_numere_pozitive(lst,n))
        elif optiune == "4":
            if ordine_crescatoare(lst) is True:
                print('DA')
            elif ordine_crescatoare(lst) is False:
                print('NU')
        elif optiune == "5":
            print(alta_lista(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()