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

def Print_Menu():
    print('1. Citire lista')
    print('2. Afiseaza lista dupa eliminarea duplicatelor')
    print('3. Calculeaza suma primelor n numere pozitive din lista')
    print('4. ')
    print('5.')
    print('x. Iesire')


def main():
    test_afisare_lista()
    test_suma_primelor_n_numere_pozitive()
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
            print()
        elif optiune == "5":
            pass
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()