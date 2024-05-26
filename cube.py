from random import randint
def cube(xDyz):
    """
    Game of cube throws.
    :param xDyz: x - how many throws, Dy - cube type (ex. D3 - three walled cube), z - optional number to '+' or '-'
    :return: the result of the cube roll(s).
    """
    throw = xDyz.split('D')  # separator 'D' podzieli wartość zmiennych na (x, yz)


    if len(throw[0]) == 0:  # jeśli długość zmiennej x = 0 czyli nie jest wyszczególniona
        par_x = 1  # wtedy parametr x przyjmuje wartość 1, tzn, że jest wykonywany jeden rzut kostką
    else:
        par_x = int(throw[0])  # Dostęp do pierwszego elementu listy

    if '+' in throw[1]:  # jeśli wystąpi modyfikator '+' w drugiej wartości zmiennej throw
        par_y, par_z = throw[1].split('+')  # wtedy należy rozdzielić wartości znakiem '+' i przypisać do zmiennych
        par_z = int(par_z)
        par_y = int(par_y)
    elif '-' in throw[1]:  # analogicznie jak wyżej
        par_y, par_z = throw[1].split('-')
        par_y = int(par_y)
        par_z = -int(par_z)
    else:  # w przypadku, kiedy parametr 'z' przyjmuje wartość 0
        par_y, par_z = throw[1].split()
        par_y=int(par_y)
        par_z = 0

    score = 0
    for _ in range(par_x):  # utworzenie pętli, która ma za zadanie wykonać tyle obrotów ile rzutów wytypował gracz
        result = randint(1, par_y)  # wynik każdego rzutu ma być wylosowany z zakresu do wartości parametru 'y'
        score += result  # dalej należy wykonać sumę rzutów
        print(f' Wynik {_+1} rzutu to: {result}')
    cube_throw = score + par_z  # w przypadku jeśli wystąpi parametr 'z' należy go dodać do ostatecznego wyniku
    return cube_throw
try:  # zabezpieczenie przed wpisaniem niewłaściwego łańcucha znaków
    user = cube("2D6+10")
    print(f'Wynik dla wybranej przez użytkownika kombinacji to: {user}')
except ValueError:
    print("Podano niewłaściwy ciąg znaków!")







