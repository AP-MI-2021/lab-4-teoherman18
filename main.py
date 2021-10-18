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


def Print_Menu():
    print('1. Citire lista')
    print('2. Afiseaza lista dupa eliminarea duplicatelor')
    print('3. ')
    print('4. ')
    print('5.')
    print('x. Iesire')


def main():
    test_afisare_lista()
    l = []
    while True:

        Print_Menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(afisare_lista(lst))
        elif optiune == "3":
            print()
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